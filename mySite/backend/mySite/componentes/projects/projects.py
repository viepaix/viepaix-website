import reflex as rx

from mySite.styles.styles import Size

cards_data = [
        {"title": "My own website", "image": "https://i.ibb.co/3sL53k0/imagge.png", "description": "I made this website using python", "repo": "https://github.com/viepaix/viepaix-website"},
        {"title": "Port Scanner in C++", "image": "https://i.ibb.co/442mK63/portscanner.png", "description": "My own port scanner created in c++", "repo": "https://github.com/viepaix/PortScanner/blob/main/portScanner.cpp"},
        {"title": "Game in Pygame", "image": "https://i.ibb.co/JctPtk1/image.png", "description": "Game style flappy bird!!", "repo": "https://github.com/viepaix/HB-game-Python?tab=readme-ov-file"},
        {"title": "Financial tracker", "image": "https://imgs.search.brave.com/7dpXdxDTRfy-CIv5XkJt-ORD5clhR89tQMzaEo2i7ss/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/dGhlYmFsYW5jZW1v/bmV5LmNvbS90aG1i/L0FWQXR6R0h2NlBy/MW5LMkdEUVNXOHpz/LWJwST0vMTUwMHgw/L2ZpbHRlcnM6bm9f/dXBzY2FsZSgpOm1h/eF9ieXRlcygxNTAw/MDApOnN0cmlwX2lj/YygpL3BpZ2d5LWJh/bmstYnVkZ2V0LTU2/YTYzNDcwM2RmNzhj/Zjc3MjhiZDNiOC5q/cGc", "description": "A financial tracker in terminal", "repo": "https://github.com/viepaix/Finance-Tracker"},
        #{"title": "", "image": "", "description": "", "repo": ""},
        #{"title": "", "image": "", "description": "", "repo": ""},
    ]

def p(card) -> rx.Component:
    return rx.card(
            rx.vstack(
            rx.heading(card["title"]),
            rx.image(src=card["image"], weight="auto", height="320px"),
            rx.hstack(
                rx.text(card["description"]),
                rx.link(
                    rx.button(rx.text("Github"), rx.icon("github")),
                    href=card["repo"],
                    is_external=True
                ),
            ),
            align_items="center",
            ),
            align="center",
            size="3"
        )

def projects() -> rx.Component:
    return rx.flex(
        rx.desktop_only(
            rx.vstack(
                rx.heading("Projects and Gallery"),
                rx.text("All my projects are open source, if you want to use something of them you are allowed, just ", 
                        rx.text.strong("give me credits"), 
                        "."),
                align="center",
                padding_top=Size.BIGGER
            ),
            rx.grid(
                *[p(card) for card in cards_data],    
                columns="3",
                spacing="4",
                align_items="center",
                width="100%",
                justify_content="center"
            )
    #rx.mobile_and_tablet(

     #   )
        ),
        margin=Size.BIGGER,
        align_items="center",
        wrap="wrap",
        align="center",
        spacing="4"

    )