import reflex as rx
import datetime

from rxconfig import config

from mysite.componentes.components import navbar
from mysite.componentes.main import header
from mysite.componentes.body import body
from mysite.componentes.footer import footer

from mysite.componentes.blogs.blogtab import accordionWithText
from mysite.componentes.projects.projects import projects as pj

from mysite.styles.styles import *

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class State(rx.State):
    """The app state."""

@rx.page(route="/404",
         title="ｼ Viepaix - 404 ｼ",
         description="Page not found. 404. Errrrrrroorrrrrr 404")
def not_found() -> rx.Component:
    return rx.center(
        rx.box(
            rx.text("➜ nmap -sV /404",
                    style={"font-family": "Ubuntu Condensed", "font-size": "4rem", "color": "#00FF00"}),
            rx.text(f"Starting Nmap 7.92 ( https://nmap.org ) at {date}",
                    style={"font-family": "Ubuntu Condensed", "font-size": "2rem", "color": "#00FF00"}),
            rx.text("Note: Host seems down. Did you mean viepaix.dev?", 
                    style={"font-family": "Ubuntu Condensed", "font-size": "2rem", "color": "#00FF00"}),
            rx.button("Go to Home",on_click=lambda: rx.redirect("/")),
            background_color="#000000",
            box_shadow="lg",
            border_radius="md",
        ),
        height="100vh",
        bg="black"
    )


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

@rx.page(route="/blog", title="ｼ Viepaix - Blog ｼ")
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
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-C9NMED7JY8"),
        rx.script("""
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-C9NMED7JY8');
                  """)
        ],
)

app.add_page(index)
