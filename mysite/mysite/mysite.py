import reflex as rx

from rxconfig import config

from mysite.componentes.components import navbar
from mysite.componentes.main import header
from mysite.componentes.body import body
from mysite.componentes.footer import footer

from mysite.componentes.blogs.blogtab import accordionWithText
from mysite.componentes.projects.projects import projects as pj

from mysite.styles.styles import *

class State(rx.State):
    selected_option: str = "default"

    def on_load(self):
        raw_path = self.router.url or ""
        if "#" in raw_path:
            self.selected_option = raw_path.split("#", 1)[1]

    def update_text(self, text: str):
        self.selected_option = text

@rx.page(route="/", 
         title="ｼ Viepaix - Main ｼ",
         description="My own website, with projects, blogs (nmap, and more soon). Viepaix is a student of Cybersecurity.")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.vstack(
            navbar(),
            padding_bottom=Size.BIGEST.value,
        ),
        rx.vstack(
            rx.box(
                header(),
                rx.desktop_only(
                    padding_bottom=Size.BIGGER.value,
                ),
            ),
            body(),
            rx.desktop_only(
                padding_bottom=Size.BIGEST.value,
            ),
            align_items="center"
        ),
        rx.vstack(
            footer(),
            align_items="center",
        ),
    )
@rx.page(route="/blog", title="ｼ Viepaix - Blog ｼ", on_load=State.on_load,)
def blog() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            padding_bottom=Size.BIGEST.value,
        ),
        rx.hstack(
            accordionWithText()
        ),
        rx.vstack(
            footer(),
            align_items="center",
        )
    )

@rx.page(route="/projects", title="ｼ Viepaix - Projects ｼ")
def projects() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            padding_bottom=Size.SMALL.value,
        ),
        rx.vstack(
            pj(),
            align_items="center"
        ),
        rx.vstack(
            footer(),
            align_items="center",
        )
    )

app = rx.App(
    style=BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
        "https://fonts.googleapis.com/css2?family=Anta&display=swap",
        "https://fonts.googleapis.com/css2?family=Expletus+Sans:ital,wght@0,400..700;1,400..700&family=Ubuntu+Condensed&display=swap"
        ],
)

app.head_components += [
    rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-C9NMED7JY8", async_=True),
    rx.script("""
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-C9NMED7JY8');
    """)
        ]

app.add_page(index)
