import reflex as rx

from mySite.styles.styles import *

def header():
    return rx.container(
            rx.desktop_only(
                rx.flex(
                    rx.hstack(
                        rx.avatar(
                            fallback="viepaix",
                            src=LOGO,
                            size="9",
                            radius="full",
                            ),
                        rx.vstack(
                            rx.heading("Hola! ｼ I'm Viepaix",
                                       size="9",
                                       style = {
                                           "font_family": "Anta"
                                           }
                                       ),
                            rx.hstack(
                                rx.text.kbd(
                                "Pentester (Junior)",
                                size="7",
                                bg=Colors.BACK
                                ),
                                padding_top=Size.SMALL
                            ),
                            padding_left=Size.DEFAULT.value,
                            align_items="center",
                        ),
                        align_items="center",
                    ),
                ),
                width="100%",
            ),
            rx.mobile_and_tablet(
                rx.box(
                    rx.flex(
                    rx.vstack(
                        rx.avatar(
                            fallback="viepaix",
                            src=LOGO,
                            size="6",
                            radius="full",
                            ),
                        rx.vstack(
                            rx.heading("Hola! ｼ I'm Viepaix", size="5", weidht="bold"),
                            rx.hstack(
                                rx.text.kbd(
                                "Pentester (Junior)",
                                size="4"
                                ),
                                padding_top=Size.SMALL
                            ),
                            align_items="center",
                        ),
                        align_items="center",
                    ),
                    ),
                    align="center",
                ),
                width="100%",
        ),
    )
