import reflex as rx

from mysite.styles.styles import *

def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(
                icon, size=22,
            ),
            rx.text(
                text, size="3", weight="medium", font_family=Fonts.UBU,
            ),
                _hover = {"color": Colors.TEXT},
        ),
        href=url,  
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
            rx.hstack(
                rx.icon(icon, size=16),
                rx.text(text, size="2", weight="medium"),
                margin=Size.SMALL.value,
            ),
            href=url,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                #LEFT SITE
                rx.hstack(
                    rx.heading(
                        MouseOver.heading_text,
                        size="7",
                        weight="bold",
                        padding_right = Size.DEFAULT.value,
                        padding_left = Size.DEFAULT.value,
                        on_mouse_enter=MouseOver.on_mouse_enter,
                        on_mouse_leave=MouseOver.on_mouse_leave,
                        
                    ),
                    navbar_icons_item(
                        "Home", "home", "/#"
                    ),
                    navbar_icons_item(
                        "Projects", "folder", "/projects"
                    ),
                    navbar_icons_item(
                        "Blogs", "newspaper", "/blog/"
                    ),
                    justify="between",
                    align_items="center",
                ),  
                # RIGHT SITE
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
                    rx.divider(orientation="vertical", size="2"),
                    rx.color_mode.button(color=Colors.ICONS),
                    justify="between",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
            justify="between",
            align_items="center",

        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.color_mode.button(color=Colors.ICONS),
                rx.hstack(
                    rx.heading(
                        "0x560x58", size="4", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=23)
                    ),
                    rx.menu.content(
                        navbar_icons_menu_item(
                            "Home", "home", "/"
                        ),
                        navbar_icons_menu_item(
                            "Projects", "folder", "/projects/"
                        ),
                        navbar_icons_menu_item(
                            "Blogs", "newspaper", "/blog/"
                        ),
                        rx.menu.sub(
                            rx.menu.sub_trigger(rx.icon("user_round", size=18),
                                                rx.text("Socials", weight="medium")
                            ),
                            rx.menu.sub_content(
                                navbar_icons_menu_item(
                                    "Github", "github", GITHUB
                                ),
                                navbar_icons_menu_item(
                                    "Twitch", "twitch", TWITCH
                                ),
                                navbar_icons_menu_item(
                                    "Instagram", "instagram", INSTAGRAM
                                ),
                                navbar_icons_menu_item(
                                    "Youtube", "youtube", YOUTUBE
                                ),
                            ),
                        ),
                        margin_top="1.5em",
                    ),
                    spacing="4",
                    dir="rtl",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style=NAVBAR,
        padding=Size.DEFAULT.value,
        position="fixed",
        z_index="20",
        margin = Size.MEDIUM.value,
        margin_top = Size.SMALL.value,
        border_radius = Size.MEDIUM.value,
        right="0",
        left="0",
    )
