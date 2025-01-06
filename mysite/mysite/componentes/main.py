import reflex as rx

from datetime import datetime, timezone
from mysite.styles.styles import *

class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    @rx.event
    def update(self):
        self.date_now = datetime.now(timezone.utc)

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
                                           },
                                       padding_bottom=".3em"
                                       ),
                            rx.hstack(
                                rx.badge(rx.icon("clock")," DFW - ", rx.moment(MomentState.date_now, format="HH:mm"), size="3", color_scheme="purple", variant="surface", margin_right=Size.SMALL),
                                rx.text.kbd(
                                "Pentester (Junior)",
                                size="6",
                                bg=Colors.BACK
                                ),
                                rx.badge(
                                    rx.icon("tag"), 
                                    "He/him", 
                                    size="3", 
                                    color_scheme="purple", 
                                    variant="surface",
                                    margin_left=Size.SMALL,
                                    ),
                            ),
                            padding_left=Size.DEFAULT.value,
                            align="center",
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
                            size="8",
                            radius="full",
                            ),
                        rx.vstack(
                            rx.heading("Hola! ｼ I'm Viepaix", size="6", align="center"),
                            rx.hstack(
                                rx.badge(
                                    rx.icon("tag", size=16), 
                                    "He/him", 
                                    size="2", 
                                    color_scheme="purple", 
                                    variant="surface",
                                    ),
                                rx.text.kbd(
                                "Pentester",
                                size="4"
                                ),
                                rx.badge(
                                    rx.icon("clock", size=16),
                                    " DFW - ", 
                                    rx.moment(MomentState.date_now, format="HH:mm"), 
                                        size="2", 
                                        color_scheme="purple", 
                                        variant="surface", 
                                ),
                                padding_top=Size.SMALL,
                            ),
                            align="center"
                        ),
                        align="center"
                    ),
                    align="center"
                    ),
                    align="center",
                ),
                width="100%",
        ),
    )
