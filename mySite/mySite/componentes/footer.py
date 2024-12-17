import reflex as rx

from mySite.styles.styles import *
from mySite.componentes.components import navbar_icons_item


def footer() -> rx.Component:
    return rx.container(
        rx.desktop_only(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.avatar(src=LOGO, radius="full"),
                        rx.heading("Viepaix", size="3"),
                        align="center"
                    ),
                    rx.card(
                        rx.hstack(
                            navbar_icons_item(
                                "", "github", GITHUB
                            ),
                            navbar_icons_item(
                                "", "twitch", TWITCH
                            ),
                            navbar_icons_item(
                                "", "instagram", INSTAGRAM
                            ),
                            navbar_icons_item(
                                "", "youtube", YOUTUBE
                            ),
                            justify="between",
                            align_items="center",
                        ),
                    ),
                        rx.link(
                            rx.button(
                                "PayPal Support", 
                                bg=Colors.ICONS, 
                                color=Colors.TEXT, 
                                high_contrast=True
                            ),
                            href=PAYPAL
                        ),
                    align="center",
                    padding_right=Size.BIGEST.value,
                ),
                rx.vstack(
                    rx.heading("Interest links", size="2"),
                    rx.link("Home", href="/"),
                    rx.link("Blog page", href="/blog"),
                    rx.link("Last Blog", href="/blog#nmap"),
                    rx.link("Last Video", href=YOUTUBE)
                ),
            )
        )
    )
