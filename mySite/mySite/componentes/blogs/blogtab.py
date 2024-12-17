import reflex as rx

from mySite.styles.styles import *

from mySite.componentes.blogs.nmap import nmap

class State(rx.State):
    selected_option: str = "default"

    def update_text(self, text: str):
        self.selected_option = text

def accordionWithText() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.vstack(
                rx.heading("Blog"),
                rx.accordion.root(
                    rx.accordion.item(
                        header="nmap",
                        content = rx.button(
                            "Introduction to nmap",
                            padding=Size.SMALL.value,
                            bg=Colors.BACK,
                            style={
                                "cursor": "pointer"
                            },
                            on_click=lambda:State.update_text("nmap")
                        )
                    ),
                    rx.accordion.item(
                        header="Soon",
                        content = rx.button(
                            "Not created yet", 
                            on_click=lambda:State.update_text("soon")
                        )
                    ),
                    rx.accordion.item(
                        header="Soon",
                        content = rx.button(rx.link("Not created yet", href="/blog/notfound"))
                    ),
                    color_scheme="purple",
                    color=Colors.TEXT,
                    width=Size.BLOGACC.value,
                    collapsible=True,
                    type="multiple"
                )
            ),
            rx.card(
                rx.flex(
                    rx.cond(
                        State.selected_option == "nmap",
                        nmap(),
                    ),
                    rx.cond(
                        State.selected_option == "soon",
                        rx.text("Visit soon")
                    ),
                    rx.cond(
                        State.selected_option == "default",
                        rx.heading("Select The blog of your interest")
                    )
                ),
                margin_left=Size.BIGEST.value,
                #margin_top=Size.DEFAULT.value
            )
        ),
        align="center",

    )
