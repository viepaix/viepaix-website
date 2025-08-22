import reflex as rx

from mysite.styles.styles import *

from mysite.componentes.blogs.nmap import nmap, nmapShortCuts
from mysite.componentes.blogs.eJPT import ejpt, notes, networkNote, linuxEsc, windowsEsc, checklist

stylesButtons = {"cursor": "pointer","width": "100%"}

class State(rx.State):
    selected_option: str = "default"

    def on_load(self):
        raw_path = self.router.url or ""
        if "#" in raw_path:
            self.selected_option = raw_path.split("#", 1)[1]

    def update_text(self, text: str):
        self.selected_option = text


def default() -> rx.Component:
    return rx.flex(
            rx.vstack(
                rx.heading("Blogs Created by Viepaix"),
                rx.text("All the blogs are 100% created by me, I like to share ideas and other things I discover daily.")
            )
    )

def accordionWithText() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.vstack(
                    rx.heading("Blog", align="center", size="7"),
                    rx.accordion.root(
                        rx.accordion.item(
                            header="eJPT",
                            content= rx.vstack(
                                rx.box(
                                    rx.button(
                                        "Introduction to eJPT",
                                        padding=Size.SMALL.value,
                                        margin_bottom=Size.SMALL,
                                        bg=Colors.ORANGE,
                                        style=stylesButtons,
                                        on_click=[
                                            State.update_text("ejpt"),
                                            rx.redirect("/blog#ejpt")
                                            ]
                                    ),
                                    rx.button(
                                        "Checklist",
                                        padding=Size.SMALL.value,
                                        margin_bottom=Size.SMALL,
                                        bg=Colors.ORANGE,
                                        style=stylesButtons,
                                        on_click=[
                                            State.update_text("checklist"),
                                            rx.redirect("/blog#checklist")
                                            ]
                                    ),
                                    rx.button(
                                        "Linux Escalation",
                                        padding=Size.SMALL.value,
                                        margin_bottom=Size.SMALL,
                                        bg=Colors.ORANGE,
                                        style=stylesButtons,
                                        on_click=[
                                            State.update_text("linuxEsc"),
                                            rx.redirect("/blog#linuxEsc")
                                            ]
                                    ),
                                    rx.button(
                                        "Windows Escalation",
                                        padding=Size.SMALL.value,
                                        margin_bottom=Size.SMALL,
                                        bg=Colors.ORANGE,
                                        style=stylesButtons,
                                        on_click=[
                                            State.update_text("windowsEsc"),
                                            rx.redirect("/blog#windowsEsc")
                                            ]
                                    ),
                                    rx.button(
                                        rx.text("Shell, Stabilization & Pivoting", size="1"),
                                        padding=Size.SMALL.value,
                                        margin_bottom=Size.SMALL,
                                        bg=Colors.ORANGE,
                                        style=stylesButtons,
                                        on_click=[
                                            State.update_text("notes"),
                                            rx.redirect("/blog#notes")
                                            ]
                                    ),
                                    rx.button(
                                        "networking",
                                        padding=Size.SMALL.value,
                                        bg=Colors.ORANGE,
                                        style=stylesButtons,
                                        on_click=[
                                            State.update_text("networking"),
                                            rx.redirect("/blog#networking")
                                            ]
                                    ),
                                ),
                            )
                        ),
                        rx.accordion.item(
                            header="nmap",
                            content = rx.box(
                                rx.button(
                                "Introduction to nmap",
                                padding=Size.SMALL.value,
                                margin_bottom=Size.SMALL,
                                bg=Colors.ORANGE,
                                style=stylesButtons,
                                on_click=[State.update_text("nmap"),
                                    rx.redirect("/blog#nmap")
                                    ]
                            ),
                            rx.button(
                                "Short Cuts",
                                padding=Size.SMALL.value,
                                bg=Colors.ORANGE,
                                style=stylesButtons,
                                on_click=[
                                    State.update_text("nmapShortCuts"),
                                    rx.redirect("/blog#nmapShortCuts")
                                    ]
                            ),
                            )
                        ),
                        rx.accordion.item(
                            header="Soon",
                            content = rx.button(
                                "Not created yet",
                                bg=Colors.ORANGE,
                                on_click=State.update_text("soon")
                            )
                        ),
                        color_scheme="purple",
                        color=Colors.TEXT,
                        width=Size.BLOGACC.value,
                        collapsible=True,
                        type="multiple",
                    ),
                    align="center",
                ),
                rx.card(
                    rx.flex(
                        rx.cond(
                            State.selected_option == "ejpt",
                            ejpt(),
                        ),
                        rx.cond(
                            State.selected_option == "checklist",
                            checklist(),
                        ),
                        rx.cond(
                            State.selected_option == "notes",
                            notes(),
                        ),
                        rx.cond(
                            State.selected_option == "linuxEsc",
                            linuxEsc(),
                        ),
                        rx.cond(
                            State.selected_option == "windowsEsc",
                            windowsEsc(),
                        ),
                        rx.cond(
                            State.selected_option == "networking",
                            networkNote(),
                        ),
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
                            default()
                        )
                    ),
                    margin_left=Size.BIGGER.value,
                    max_width="70rem",
                    align="center",
                ),
            ),
            width="100%",
            align="center",
            padding_left=Size.BIGEST.value,
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
                                             on_click=State.update_text("nmap")
                                ),
                                rx.menu.item("Short Cuts",
                                             on_click=State.update_text("nmapShortCuts")
                                ),
                            ),
                        ),
                        rx.menu.separator(),
                        rx.menu.item("Soon", on_click=State.update_text("soon"), color="red")
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
