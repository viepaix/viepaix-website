import reflex as rx

from typing import List

text = "Amor, if you are reading this you know why I made this. I just want to say that I love you so much and you are the best person that has ever happened to me. You make me so happy and I am so grateful to have you in my life. I hope you like this little surprise I made for you. You are my everything and I can't wait to continue my days with you and sharing time with the person I most love. Te amo con todo mi corazón."

class ForeachState(rx.State):
    cute_things: List[str] = ["You're my favorite person", "I love your smile", "You make me happy", "Always better with you", "My heart is yours", "You're my safe place", "I think about you all the time", "You're my sunshine daily", "Love being with you", "You're my sweetest dream", "You make life brighter", "You're my whole world", "I'm lucky it's you", "You're my happy thought", "I choose you always", "Your mine", " you are the girl I always wanted"]

class State(rx.State):
    image_index: int = 0
    text_index: int = 0
    user_input: str = ""
    show_message: bool = False

    messages: list[str] = [
        "AAAAAA I LOVE YOU, BUT CHECK THE OTHERS",
        "YO TE AMO MUCHO MAS Y ME HACES MUY FELIZ",
        "THIS MIGHT BE THE BEST DAY SINCE I MEET YOU BBY",
        "NO WAYYYYY COME WITH ME BBY, I WANT TO HUG YOU SO BADLY AND YOU ARE EVERYTHING I WANTED EVER",
    ]

    images: list[str] = [
    "/maya/maya1.jpg", "/maya/maya2.jpg", "/maya/maya3.jpg", "/maya/maya4.jpg", "/maya/maya5.jpg", "/maya/maya6.jpg", "/maya/nightlove.jpg"
    ]

    texts: list[str] = [
        "look at you so beautiful",
        "Te amo, tenerte junto a mi me hace sentir super feliz y afortunado",
        "My little girl, you are so special to me.",
        "Hugs from you are my favorite and I don't let anyone hug me like you do",
        "Love going out with you, even if it is just for 5 minutes",
        "Your eyes are so beautiful is like looking at the stars",
        "Those cozy nights with you are the best, they make me feel so loved and happy like it is HOME",
            ]

    def check_input(self):
        if self.user_input.lower() == "santiago":
            self.show_message = True
        else:
            self.show_message = False

    def nextImage(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.text_index = (self.text_index + 1) % len(self.texts)

    def prevImage(self):
        self.image_index = (self.image_index - 1) % len(self.images)
        self.text_index = (self.text_index - 1) % len(self.texts)



def maya() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.heading("❤︎ Maya irfan ❤︎", size="9", color_scheme="pink"),
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
                rx.vstack(
                    rx.heading("This is only for you my love", size="6", color="white", align="center"),
                    rx.text(text, size="4", align="center", color="black"),
                    align="center",
                ),
                padding="6em",
                style={
                    "background": "radial-gradient(circle at top left, #c91c8d, #e01499, #e85dc8, #e85da9)",
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
                    padding_right="8em",
                ),
                rows="1",
                columns="2",
                align="center",
                justify="center",
                padding_top="3em",
            ),
            rx.container(
                rx.vstack(
                    rx.heading("Some of my favorite photos of you and also us together", size="7", align="center"),
                    rx.blockquote("Tap on the image to reveal a message", size="4", weight="bold", color_scheme="pink"),
                    rx.box(
                        rx.card(
                            rx.vstack(
                                rx.popover.root(
                                    rx.popover.trigger(
                                        rx.image(src=State.images[State.image_index], width="400px", border_radius="20px",),
                                    ),
                                    rx.popover.content(
                                        rx.text(State.texts[State.text_index], size="4", padding="1em", align="center"),
                                        rx.popover.close(
                                            rx.button("Close", color_scheme="pink", align="end"),
                                        ),
                                        side="bottom",
                                    ),
                                    rx.hstack(
                                        rx.button("Previous", on_click=State.prevImage, color_scheme="pink", variant="outline", radius="full", size="3"),
                                        rx.heading(f"Image {State.image_index + 1} of {State.images.length()}", size="4", color="white",align="center"),
                                        rx.button("Next", on_click=State.nextImage, color_scheme="pink", variant="outline", radius="full", size="3"),
                                        justify="between",
                                        align="center",
                                    ),
                                ),
                            align="center",
                            ),
                            width="570px",
                            align="center",
                            style={"box-shadow": "0 0 2rem pink"},
                        ),
                        padding_top="3em",
                    ),
                    align="center",
                ),
                padding_top="8em",
                padding_bottom="3em"
            ),
            rx.container(
                rx.vstack(
                    rx.heading("I have", rx.heading("something", color_scheme="purple", size="9"), "to ask you...", size="9", align="center"),
                    rx.text("First tell me the name of the person who you love", size="7", align="center"),
                    rx.hstack(
                        rx.input(
                            placeholder="Type here...",
                            value=State.user_input,
                            variant="soft",
                            radius="full",
                            size="3",
                            on_change=State.set_user_input,
                            align="center",
                        ),
                        rx.button("Check", on_click=State.check_input, color_scheme="purple", align="center", radius="full", variant="solid", size="3"),
                        align="center",
                        padding_top="2em",
                    ),
                    rx.cond(
                        State.show_message,
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button("Surprise ❤︎", color_scheme="purple", align="center", size="4", variant="solid", radius="full"),
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.text("Maya, would you", rx.text.strong(" be my girlfriend?", color="orange"), " ❤︎", size="8", padding="1em", align="center"),
                                    rx.hstack(
                                        rx.button("Yes I love you", variant="outline", color_scheme="pink", on_click=rx.toast(State.messages[0], duration=7000, position="bottom-right", important=True)),
                                        rx.button("si, te amo", variant="outline",color_scheme="pink", on_click=rx.toast(State.messages[1], duration=7000, position="bottom-right", important=True)),
                                        rx.button("obviusly yes",variant="outline", color_scheme="pink", on_click=rx.toast(State.messages[2], duration=7000, position="bottom-right", important=True)),
                                        align="center",
                                    ),
                                    rx.popover.close(
                                        rx.button("YES! and I will give you a kiss", variant="outline", color_scheme="pink", align="end", on_click=rx.toast(State.messages[3], duration=7000, position="top", important=True)),
                                    ),
                                    align="center",
                                ),
                                box_shadow="0 0 2rem pink",
                                side="top",
                                size="4"
                            ),
                        )
                    ),
                    align="center",
                ),
                padding_top="4em",
                background="linear-gradient(to bottom, #ff9eb5, #ff8ebc, #ff3ed0)" ,
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("❤︎  Maya irfan ❤︎", size="7"),
                rx.center(
                    rx.box(
                        rx.foreach(
                            ForeachState.cute_things,
                            lambda thing: rx.badge(thing, color_scheme="pink", align="center", margin="7px"),
                        ),
                    ),
                ),
                align="center",
                padding_top="2em",
            ),
            rx.center(
                rx.vstack(
                    rx.heading("This is only for you my love", size="6", color="white", align="center"),
                    rx.text(text, size="4", align="center"),
                    align="center",
                ),
                padding="2em",
                style={
                    "background": "radial-gradient(circle at top left, #c91c8d, #e01499, #e85dc8, #e85da9)",
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
            rx.container(
                rx.vstack(
                    rx.heading("Some of my favorite photos of you and also us together", size="6", align="center"),
                    rx.blockquote("Tap on the image to reveal a message", size="4", weight="bold", color_scheme="pink"),
                    rx.box(
                    rx.card(
                        rx.vstack(
                            rx.popover.root(
                                rx.popover.trigger(
                                    rx.image(src=State.images[State.image_index], width="300px", border_radius="20px",),
                                ),
                                rx.popover.content(
                                    rx.text(State.texts[State.text_index], size="3", padding="1em", align="center"),
                                    rx.popover.close(
                                        rx.button("Close", color_scheme="pink", align="end"),
                                    ),
                                    side="bottom",
                                ),
                                rx.hstack(
                                    rx.button("Previous", on_click=State.prevImage, color_scheme="pink", variant="outline", radius="full", size="3"),
                                    rx.heading(f"Image {State.image_index + 1} of {State.images.length()}", size="2", color="white", align="center"),
                                    rx.button("Next", on_click=State.nextImage, color_scheme="pink", variant="outline", radius="full", size="3"),
                                    justify="between",
                                    align="center",
                                ),
                            ),
                        align="center",
                        ),
                        align="center",
                        style={"box-shadow": "0 0 2rem pink"},
                        ),
                        padding_top="2em",
                    ),
                    align="center",
                ),
                padding_top="3em",
                padding_bottom="3em"
            ),
            rx.container(
                rx.vstack(
                    rx.heading("I have", rx.heading("something", size="7", color_scheme="purple"), "to ask you...", size="7", align="center"),
                    rx.text("First tell me the name of the person who you love", size="4", align="center"),
                    rx.hstack(
                        rx.input(
                            placeholder="Type here...",
                            value=State.user_input,
                            on_change=State.set_user_input,
                            align="center",
                        ),
                        rx.button("Check", on_click=State.check_input, color_scheme="pink", align="center"),
                        align="center",
                        padding_top="2em",
                    ),
                    rx.cond(
                        State.show_message,
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button("Click here ❤︎", color_scheme="pink", align="center"),
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.text("Maya, would you", rx.text.strong(" be my girlfriend? ", color="orange"), "❤︎", size="5", padding="1em", align="center"),
                                    rx.hstack(
                                        rx.button("Yes I love you", color_scheme="pink", variant="outline", on_click=rx.toast(State.messages[0], duration=5000, position="top", important=True)),
                                        rx.button("si, te amo", color_scheme="pink", variant="outline", on_click=rx.toast(State.messages[1], duration=5000, position="top", important=True)),
                                        rx.button("obviusly yes", color_scheme="pink", variant="outline", on_click=rx.toast(State.messages[2], duration=5000, position="top", important=True)),
                                        align="center",
                                    ),
                                    rx.popover.close(
                                        rx.button("YES! and I will give you a kiss", color_scheme="pink", variant="outline", align="end", on_click=rx.toast(State.messages[3], duration=5000, position="top", important=True))
                                    ),
                                    align="center",
                                ),
                                side="bottom",
                            ),
                        )
                    ),
                    align="center",
                ),
                padding_top="3em",
                padding_bottom="6em",
                background="linear-gradient(to bottom, #ff9eb5, #ff8ebc, #ff3ed0)" ,
            )
        ),
    )
