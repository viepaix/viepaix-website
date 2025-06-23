import reflex as rx

import datetime

from mysite.styles.styles import *

birthday = datetime.date(2004, 6, 20)  # Replace with your actual birthday

year = datetime.date.today().year - birthday.year

if (datetime.date.today().month, datetime.date.today().day) < (birthday.month, birthday.day):
    year -= 1

text = f"My name is Santiago, I'm {year} years old and currently studying Cybersecurity and Pentesting, aiming to earn the eJPTv2 certification. I create content on hacking, programming, and pentesting for my YouTube channel. Passionate about technology, I’m constantly learning and seeking new challenges and opportunities to grow in cybersecurity and programming."

text2 = "My dream is to become not just a skilled hacker and programmer, but a well-rounded professional in cybersecurity. I’m driven by the goal of making a real impact—both in the tech world and in the lives of those I care about. Above all, I want to grow, support my family in every way I can, and build a meaningful path in life."

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
            rx.center(
                rx.vstack(
                     rx.html("""
                        <style>
                            @keyframes fadeIn {
                                from { opacity: 0; }
                                to { opacity: 1; }
                            }

                            .fade-heading {
                                animation: fadeIn 3s ease-in forwards;
                            }
                        </style>
                    """),
                    rx.heading("Get your Website", size="7", color=Colors.TEXT, align="center", class_name="fade-heading"),
                    rx.text(
                        "Your ideas deserve more than a template. I craft custom websites that don’t just look great — they work hard for you. Fast, sleek, and built from scratch to match your goals. Let’s turn your vision into something real.",
                        align="center",
                        width="70%",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon("twitter"),
                                rx.text("Dm me on Twitter"),
                            ),
                            href=X,
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                rx.icon("github"),
                                rx.text("Check my GitHub"),
                            ),
                            href=GITHUB,
                            is_external=True,
                        ),
                        align="center",
                    ),
                    rx.html("""
                <style>
                    @keyframes flyRight {
                        0% { left: 0%; opacity: 1; }
                        70% { left: 64%; opacity: 0.6; }
                        80% { left: 70%; opacity: 0.4; }
                        100% { left: 90%; opacity: 0;  }
                    }
                    .fly {
                        animation: flyRight 8s linear infinite;
                        width: 10%;
                        position: absolute;
                    }
                </style>
                    """),
                    rx.html('<img src="/flying.gif" class="fly" />'),
                    align="center",
                ),
                padding_bottom=Size.BIGEST,
            ),
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
                ),
                    rx.vstack(
                        rx.heading(
                            "Developing My own Tools",
                            align="center",
                        ),
                        rx.link(
                            rx.card(
                                rx.inset(
                                    rx.image(src="/githubprofile.png", width="100%", height="auto",
                                             style={"_hover":
                                                    {"transform": "scale(1.4)"},
                                                    "transition": "transform 0.3s",
                                                 }),
                                    side="top",
                                    pb=Size.DEFAULT.value,
                                ),
                                rx.text("Python hacking programming and pentesting", align="center", high_contrast=True),
                            ),
                            href="https://github.com/viepaix/",
                            is_external=True,
                        ),
                width="85%",
                align="center",
                padding_top=Size.SMALL,
                ),
                columns="2",
                width="100%",
                align_items="flex-start",
            ),
            rx.flex(
                rx.vstack(
                rx.hstack(
                    rx.heading("Skills", align="center", align_items="center", size="7"),
                    rx.avatar(src=COFFEE, size="1"),
                ),
            rx.grid(
                rx.hstack(
                    languages(),
                ),
                rx.hstack(
                    tools(),
                ),
                rx.hstack(
                    frameworks_os(),
                ),
                columns="3",
                spacing="4",
                width="100%",
                ),
            align="center",
                ),
            padding_top=Size.BIGGER,
            ),
            rx.vstack(
                rx.heading("=--= | Video of Youtube | =--=", size="7", margin_bottom=Size.DEFAULT),
                    rx.video(
                        url="https://youtu.be/awY_kKi5dpM",
                        playing=True,
                        volume=0,
                        width="1080px",
                        height="720px",
                    style = {
                        "box_shadow": "0px 0px 30px 0.5px pink",
                    },
                    ),
                padding_top=Size.BIGGER,
                align="center"  
            ),
            align="center",
            width="1160px"
        ),
        rx.mobile_and_tablet(
            rx.center(
                rx.vstack(
                    rx.html("""
                        <style>
                            @keyframes fadeIn {
                                from { opacity: 0; }
                                to { opacity: 1; }
                            }

                            .fade-heading {
                                animation: fadeIn 3s ease-in forwards;
                            }
                        </style>
                    """),
                    rx.heading("Get your Website", size="7", color=Colors.TEXT, align="center", class_name="fade-heading"),
                    rx.text(
                        "Your ideas deserve more than a template. I craft custom websites that don’t just look great — they work hard for you. Fast, sleek, and built from scratch to match your goals. Let’s turn your vision into something real.",
                        align="center",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon("twitter"),
                                rx.text("Dm me on Twitter"),
                            ),
                            href=X,
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                rx.icon("github"),
                                rx.text("Check my GitHub"),
                            ),
                            href=GITHUB,
                            is_external=True,
                        ),
                        align="center",
                    ),
                    rx.center(
                        rx.html("""
                    <style>
                        @keyframes flyRight {
                            0% { left: 0%; opacity: 1; }
                            20% { left: 40%; opacity: 0.6; }
                            50% { left: 60%; opacity: 0.4; }
                            70% { left: 70%; opacity: 0;  }
                            100% { transform: translateX(calc(60vw - 60vw)); opacity: 0; }
                        }
                        .fly {
                            animation: flyRight 7s linear infinite;
                            width: 20vw;
                            position: absolute;
                        }
                    </style>
                        """),
                        rx.html('<img src="/flying.gif" class="fly" />'),
                        max_width="100px",
                    ),
                    align="center",
                ),
                align="center",
            ),
            rx.grid(
                rx.vstack(
                    rx.center(
                    rx.card(
                        rx.center(
                            rx.hstack(
                                rx.heading("About me", color=Colors.TEXT),
                                rx.avatar(src=AVATAR, size="1"),
                                padding_bottom=Size.SMALL,
                            ),
                        align="center",
                        ),
                        rx.text(text, align="center", high_contrast=True),
                        align="center",
                    ),
                    align="center",
                    padding=Size.MEDIUM.value
                    ),
                    rx.vstack(
                        rx.heading("= | Video of Youtube | =", size="2", padding_bottom=Size.DEFAULT),
                        rx.video(
                            url="https://youtu.be/awY_kKi5dpM",
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

