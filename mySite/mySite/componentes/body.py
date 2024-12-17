import reflex as rx

import datetime

from mySite.styles.styles import *

year = datetime.date.today().year - 2004

text = f"My name is Santiago, I have {year} years old and I am a student of CyberSecurity, Pentesting, Hack4u student. From Colombia, actually in the U.S. trying to live and be someone, learning programming languages and new things all the days."

def languages():
    return rx.card(
            rx.hstack(
                rx.heading("Languages", padding_bottom=Size.SMALL.value),
                rx.avatar(src="https://img.icons8.com/?size=100&id=43988&format=png&color=000000", size="3")
            ),
            rx.hstack(
                rx.avatar(src=BASH, size="1"),
                rx.blockquote("Bash", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=CPP, size="1"),
                rx.blockquote("C++", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=PYTHON, size="1"),
                rx.blockquote("Python", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=HTML, size="1"),
                rx.blockquote("HTML", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=CSS, size="1"),
                rx.blockquote("CSS", weight="bold")
            ),
            rx.hstack(
                rx.avatar(src=MD, size="1"),
                rx.blockquote("MarkDown", weight="bold")
            ),
        )

def tools():
    return rx.card(
            rx.hstack(
                rx.heading("Tools", padding_bottom=Size.SMALL.value),
                rx.avatar(src="https://img.icons8.com/?size=100&id=43630&format=png&color=000000", size="3")
                ),
            rx.hstack(
                rx.avatar(src=GIT, size="1"),
                rx.blockquote("GIT", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=GITHUBLOGO, size="1"),
                rx.blockquote("GITHUB", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=NEOVIM, size="1"),
                rx.blockquote("Neovim", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=OBSIDIAN, size="1"),
                rx.blockquote("Obsidian", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=POWERSHELL, size="1"),
                rx.blockquote("Powershell", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
            rx.hstack(
                rx.avatar(src=VSCODE, size="1"),
                rx.blockquote("VisualStudio Code", weight="bold"),
                padding_bottom=Size.SMALLER
            ),
    )

def frameworks_os():
    return rx.card(
            rx.desktop_only(
                rx.hstack(
                    rx.heading("OS and Others", padding_bottom=Size.SMALLER.value),
                    rx.avatar(src="https://img.icons8.com/?size=100&id=55485&format=png&color=000000", size="3")
                ),
                rx.hstack(
                    rx.container(
                        rx.hstack(
                            rx.avatar(src=WINDOWS, size="1"),
                            rx.blockquote("Windows", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=LINUX, size="1"),
                            rx.blockquote("Linux", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),        
                        rx.hstack(
                            rx.avatar(src=UBUNTU, size="1"),
                            rx.blockquote("Ubuntu", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),        
                        rx.hstack(
                            rx.avatar(src=DEBIAN, size="1"),
                            rx.blockquote("Debian", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),        
                        rx.hstack(
                            rx.avatar(src=KALI, size="1"),
                            rx.blockquote("Kali", weight="bold"),
                        ),
                    ),
                    rx.container(
                        rx.hstack(
                            rx.avatar(src=PHOTOSHOP, size="1"),
                            rx.blockquote("Photoshop", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=REGEX, size="1"),
                            rx.blockquote("Regex", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=WORDPRESS, size="1"),
                            rx.blockquote("WordPress", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=AMAZON, size="1"),
                            rx.blockquote("Amazon Web Services", weight="bold")
                        ),
                    ),
                )
            ),
            rx.mobile_and_tablet(
                rx.hstack(
                    rx.heading("OS and Others", padding_bottom=Size.SMALLER.value),
                    rx.avatar(src="https://img.icons8.com/?size=100&id=55485&format=png&color=000000", size="3")
                ),
                rx.hstack(
                    rx.container(
                        rx.hstack(
                            rx.avatar(src=WINDOWS, size="1"),
                            rx.blockquote("Windows", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=LINUX, size="1"),
                            rx.blockquote("Linux", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),        
                        rx.hstack(
                            rx.avatar(src=UBUNTU, size="1"),
                            rx.blockquote("Ubuntu", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),        
                        rx.hstack(
                            rx.avatar(src=DEBIAN, size="1"),
                            rx.blockquote("Debian", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),        
                        rx.hstack(
                            rx.avatar(src=KALI, size="1"),
                            rx.blockquote("Kali", weight="bold"),
                        ),
                        rx.hstack(
                            rx.avatar(src=PHOTOSHOP, size="1"),
                            rx.blockquote("Photoshop", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=REGEX, size="1"),
                            rx.blockquote("Regex", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=WORDPRESS, size="1"),
                            rx.blockquote("WordPress", weight="bold"),
                            padding_bottom=Size.SMALLER
                        ),
                        rx.hstack(
                            rx.avatar(src=AMAZON, size="1"),
                            rx.blockquote("Amazon Web Services", weight="bold")
                        ),
                    )
                )
            )
    )

def body() -> rx.Component:
    return rx.flex(
        rx.desktop_only(
            rx.grid(
                rx.vstack(
                    rx.box(
                    rx.card(
                        rx.hstack(
                            rx.heading("About me", color=Colors.TEXT),
                            rx.avatar(src=AVATAR, size="2"),
                            padding_bottom=Size.SMALL
                        ),
                        rx.text(text, align="left", high_contrast=True),
                        size="3",
                        width="80%",
                        align_items="right",
                    ),
                        padding_bottom=Size.MEDIUM
                    ),
                    rx.vstack(
                        rx.heading("=--= | Video of Youtube | =--=", size="3", padding_bottom=Size.DEFAULT),
                        rx.video(
                            url="https://www.youtube.com/embed/f1wHduNsqIQ",
                            width="495px",
                            height="300px",
                        ),
                        align="center"
                    ),
                ),
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Skills", align="center", align_items="center", size="7"),
                            rx.avatar(src=COFFEE, size="2"),
                        ),
                        rx.hstack(
                            languages(),
                            tools(),
                        ),
                        rx.hstack(
                            frameworks_os(),
                        ),
                        align_items="center",
                    ),
                    size="5"
                ),
                columns="2",
                width="100%",
                align_items="flex-start",
                justify_items="center",
            ),
            align_items="center",
            width="1260px"
        ),
        rx.mobile_and_tablet(
            rx.grid(
                rx.vstack(
                    rx.box(
                    rx.card(
                        rx.hstack(
                            rx.heading("About me", color=Colors.TEXT, align="center"),
                            rx.avatar(src=AVATAR, size="1"),
                            padding_bottom=Size.SMALL,
                            align="center"
                        ),
                        rx.text(text, align="center", high_contrast=True),
                        margin="30px",
                        size="1",
                    ),
                        padding_bottom=Size.MEDIUM
                    ),
                    rx.vstack(
                        rx.heading("| Video of Youtube |", size="1", padding_bottom=Size.DEFAULT),
                        rx.video(
                            url="https://www.youtube.com/embed/f1wHduNsqIQ",
                            width="385px",
                            height="auto"
                        ),
                        align="center"
                    ),
                    padding_bottom=Size.DEFAULT,
                    align="center"
                ),
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Skills", align="center", align_items="center", size="7"),
                            rx.avatar(src=COFFEE, size="2"),
                        ),
                        rx.vstack(
                            languages(),
                            tools(),
                            frameworks_os(),
                        ),
                        align="center",
                    ),
                    align="center",
                    size="1"
                ),
                columns="1",
                align="center",
                margin="10px"
            ),
            align="center",
        )
    )

