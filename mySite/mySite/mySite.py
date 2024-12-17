import reflex as rx

from rxconfig import config

from mySite.componentes.components import navbar
from mySite.componentes.main import header
from mySite.componentes.body import body
from mySite.componentes.footer import footer

from mySite.componentes.blogs.blogtab import accordionWithText

from mySite.styles.styles import *

class State(rx.State):
    """The app state."""

    ...

@rx.page(route="/", title="ｼ Viepaix - Main ｼ")
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
                padding_bottom=Size.BIGGER.value,
            ),
            body(),
            align_items="center",
            padding_bottom=Size.BIGEST.value,
        ),
        rx.vstack(
            footer(),
            align_items="center"
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
            align_items="center"
        )
    )

@rx.page(route="/projects", title="ｼ Viepaix - Projects ｼ")
def projects() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
        ),
        rx.vstack(
            footer(),
            align_items="center"
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

app.add_page(index)
app.add_page(blog)
