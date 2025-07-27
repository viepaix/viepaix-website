import reflex as rx

import datetime

from mysite.styles.styles import *

year = datetime.date.today().year - 2004

text = f"My name is Santiago, I'm {year} years old and I am a student of CyberSecurity, Pentesting, Hack4u student. From Colombia, actually in the U.S. trying to live and be someone, learning programming languages and new things all the days."

text2 = "My dream is to be a great hacker, programmer, and person, I want to be a great professional in the area of cybersecurity and programming, help my family in all the ways that I can, and be someone in life."

def languages():
    return rx.card(
            rx.heading(
                "Languages ",
                rx.avatar(src="https://img.icons8.com/?size=100&id=43988&format=png&color=000000", size="3"),
                align="center", 
                margin_bottom=Size.SMALL.value
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
            width="100%",
            align="center"
        )

def tools():
    return rx.card(
            rx.heading(
                "Tools ",
                rx.avatar(src="https://img.icons8.com/?size=100&id=43630&format=png&color=000000", size="3"),
                margin_bottom=Size.SMALL.value,
                align="center"
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
            width="100%"
    )

def frameworks_os():
    return rx.card(
            rx.desktop_only(
                rx.heading(
                    "OS and Others ",
                    rx.avatar(src="https://img.icons8.com/?size=100&id=55485&format=png&color=000000", size="3"),
                    margin_bottom=Size.SMALLER.value,
                    align="center"
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
                rx.heading(
                    "OS and Others",
                    padding_bottom=Size.SMALLER.value,
                    align="center"
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
                    ),
                    width="100%"
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
                            rx.heading("About me"),
                            rx.avatar(src=AVATAR, size="2"),
                            justify_content="center",
                            align="center",
                            margin_bottom=Size.SMALL
                        ),
                        rx.text(text, align="center", high_contrast=True, size="4"),
                        width="85%",
                    ),
                    align="center",
                    padding_bottom=Size.MEDIUM
                    ),
                    rx.vstack(
                        rx.heading("My Dream", color=Colors.TEXT),
                        rx.text(text2, align="center", high_contrast=True, size="4"),
                        width="85%",
                        align="center",
                        ),
                    rx.vstack(
                        rx.heading("Working on"),
                        rx.hstack(
                            rx.card(
                                rx.inset(
                                    rx.image(src=PYTHON_IMAGE, width="100%", height="auto",
                                             style={"_hover":
                                                    {"transform": "scale(1.4)"},
                                                    "transition": "transform 0.3s",
                                                 }),
                                    side="top",
                                    pb=Size.SMALL.value,
                                ),
                                rx.text("Python hacking programming and pentesting", align="center", high_contrast=True),
                            ),
                        ),
                        width="85%",
                        align="center",
                        padding_top=Size.DEFAULT,
                    ),
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
                        align_items="center",
                    ),
                    size="4"
                ),
                columns="2",
                width="100%",
                align_items="flex-start",
            ),
            rx.vstack(
                rx.heading("=--= | Video of Youtube | =--=", size="7", margin_bottom=Size.DEFAULT),
                    rx.video(
                        url="https://www.youtube.com/embed/-V1t0eHhQGo",
                        playing=True,
                        volume=0,
                        width="1080px",
                        height="720px",
                    style = {
                        "box_shadow": "0px 0px 30px 0.5px purple",
                    },
                    ),
                padding_top=Size.BIGGER,
                align="center"  
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
                        padding_bottom=Size.DEFAULT
                    ),
                    rx.vstack(
                        rx.heading("=-= | Video of Youtube | =-=", size="2", padding_bottom=Size.DEFAULT),
                        rx.video(
                            url="https://www.youtube.com/embed/-V1t0eHhQGo",
                            playing=True,
                            controls=True,
                            volume=0,
                            width="auto",
                            height="175px",
                            style = {
                                "box_shadow": "0px 0px 30px 0.5px purple",
                                "z_index": "-1"
                            }
                        ),
                        align="center"
                    ),
                    padding_bottom=Size.MEDIUM,
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
                            align="center",
                        ),
                        align="center",
                    ),
                    align="center",
                    size="1",
                    margin="16px"
                ),
                columns="1",
                align="center",
                margin="16px"
            ),
            align="center",
        )
    )

