import reflex as rx

from typing import List


text = "Amor, if you are reading this you know why I made this. I just want to say that I love you so much and you are the best thing that has ever happened to me. You make me so happy and I am so grateful to have you in my life. I hope you like this little surprise I made for you. You are my everything and I can't wait to continue my days with you and sharing time with the person I love. Te amo con todo mi corazón."

class ForeachState(rx.State):
    cute_things: List[str] = ["You're my favorite person", "I love your smile", "You make me happy", "Always better with you", "My heart is yours", "You're my safe place", "I think about you all the time", "You're my sunshine daily", "Love being with you", "You're my sweetest dream", "You make life brighter", "You're my whole world", "I'm lucky it's you", "You're my happy thought", "I choose you always", "Your mine", " you are the girl I always wanted"]


def maya() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.heading("Maya irfan", size="9"),
                rx.center(
                    rx.container(
                        rx.foreach(
                            ForeachState.cute_things,
                            lambda thing: rx.badge(thing, color_scheme="pink", align="center", margin="7px"),
                        ),
                    )
                ),
                padding_top="3em",
                align="center",
            ),
            rx.center(
                rx.text(text, size="5", align="center", color="black"),
                padding="8em",
                style={
                    "background": "radial-gradient(circle at top left, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e)",
                }
            ),
            rx.grid(
                rx.center(
                    rx.image(src="/maya/amormio.jpg", width="400px", align="center", border_radius="20px",
                             style={"filter": "drop-shadow(0 0 0.60rem pink)"}
                    ),
                ),
                rx.vstack(
                    rx.heading("The first Hello", size="8"),
                    rx.text("I wanted to remember tyhe first day when I said hello (", rx.text.strong("August 5th at 8:40PM"), ") when you asked me if I were Colombian, and yes I'm the only one that will be always there for you no matter what", size="4", align="center"),
                    align="center",
                ),
                spacing_x="0",
                rows="1",
                columns="2",
                align="center",
                justify="start",
                padding_top="3em",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("Maya irfan", size="7"),
                rx.center(
                    rx.box(
                        rx.foreach(
                            ForeachState.cute_things,
                            lambda thing: rx.badge(thing, color_scheme="pink", align="center", margin="7px"),
                        ),
                    ),
                ),
                align="center",
            ),
            rx.center(
                rx.text(text, size="4", align="center"),
                padding="2em",
                style={
                    "background": "radial-gradient(circle at top left, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e)",
                }
            ),
            rx.separator(
                color_scheme="pink",
                decorative=True,
            ),
            rx.vstack(
                rx.heading("The first Hello", size="6"),
                rx.text("I wanted to remember tyhe first day when I said hello (", rx.text.strong("August 5th at 8:40PM"), ") when you asked me if I were Colombian, and yes I'm the only one that will be always there for you no matter what", size="3", align="center"),
                rx.image(src="/maya/amormio.jpg", width="300px", align="center", border_radius="20px", padding_top="1em",
                         style={"filter": "drop-shadow(0 0 0.60rem pink)"}
                ),
                align="center",
                padding_top="3em",
                padding_bottom="3em"
            ),

        )
    )
