import reflex as rx

from mySite.styles.styles import *

from mySite.componentes.blogs.nmap import nmap, nmapShortCuts

class State(rx.State):
    selected_option: str = "default"

    def update_text(self, text: str):
        self.selected_option = text

def accordionWithText() -> rx.Component:
    return rx.container(
        rx.desktop_only(
            rx.hstack(
                rx.vstack(
                    rx.heading("Blog"),
                    rx.accordion.root(
                        rx.accordion.item(
                            header="nmap",
                            content = rx.box(
                                rx.button(
                                "Introduction to nmap",
                                padding=Size.SMALL.value,
                                bg=Colors.BACK,
                                style={
                                    "cursor": "pointer"
                                },
                                on_click=lambda:State.update_text("nmap")
                            ),
                            rx.button(
                                "Short Cuts",
                                padding=Size.SMALL.value,
                                bg=Colors.BACK,
                                style={
                                    "cursor": "pointer"
                                },
                                on_click=lambda:State.update_text("nmapShortCuts")
                            ),
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
                            State.selected_option == "nmapShortCuts",
                            nmapShortCuts(),
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
                )
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.hstack(
                            rx.text('Blogs'),
                            rx.icon("menu", size=22),
                            bg=Colors.BACK,
                            padding="7px",
                            style=NAVBAR2,

                        )
                    ),
                    rx.menu.content(
                        rx.menu.sub(
                            rx.menu.sub_trigger("Nmap"),
                            rx.menu.sub_content(
                                rx.menu.item("Introduction",
                                             on_click=lambda:State.update_text("nmap")
                                ),
                                rx.menu.item("Short Cuts",
                                             on_click=lambda:State.update_text("nmapShortCuts")
                                ),
                            ),
                        ),
                        rx.menu.separator(),
                        rx.menu.item("Soon", on_click=lambda:State.update_text("soon"), color="red")
                    )
                ),
                top="5.5em",
                position="fixed",
                z_index="19"
            ),
            rx.card(
                rx.flex(
                    rx.cond(
                        State.selected_option == "nmap",
                        nmap(),
                    ),
                    rx.cond(
                        State.selected_option == "nmapShortCuts",
                        nmapShortCuts(),
                    ),
                    rx.cond(
                        State.selected_option == "soon",
                        rx.text("Visit soon")
                    ),
                    rx.cond(
                        State.selected_option == "default",
                        rx.heading("Select The blog of your interest", size="1")
                    )
                ),
            )
        )
    )
