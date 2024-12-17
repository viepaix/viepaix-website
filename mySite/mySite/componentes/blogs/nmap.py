import reflex as rx

from mySite.styles.styles import *

def nmap() -> rx.Component:
    return rx.box(
            rx.desktop_only(
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Introduction to Nmap", size="5"),
                            rx.avatar(src="https://www.liquidweb.com/wp-content/uploads/2024/03/nmap-logo-256x256-1.avif", size="4")
                        ),
                        rx.markdown("First let see *`what is nmap?`*"),
                        rx.text("Nmap is a Tool created for scanning a network such as discover hosts, ports and also can be used to detect OS version. The creator is ", rx.link("Gordon Lyon", href="https://en.wikipedia.org/wiki/Gordon_Lyon")
                        ),
                        rx.vstack(
                            rx.heading("Short Cuts", 
                                       size="2",
                                       padding_top=Size.MEDIUM.value),
                            rx.blockquote(rx.code("nmap [scan type] [options] [target]", color_scheme="violet", variant="ghost", high_contrast=True), color_scheme="violet"),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Syntax"),
                                        rx.table.column_header_cell("Example"),
                                        rx.table.column_header_cell("Description")
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.row_header_cell("-p", color=Colors.TEXT),
                                        rx.table.cell("nmap -p 23 127.0.0.0"),
                                        rx.table.cell("Scan specific port")
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell("-p [range]", color=Colors.TEXT),
                                        rx.table.cell("nmap -p 23-445 127.0.0"),
                                        rx.table.cell("Scan a range of ports")
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell("-p-", color=Colors.TEXT),
                                        rx.table.cell("nmap -p- 127.0.0.0"),
                                        rx.table.cell("Scan all ports")
                                    ),
                                )
                            ),
                        width="100%",
                        align="center"
                        )
                    ),
                direction="column",
            ),
            id="nmap"
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                        rx.hstack(
                            rx.heading("Introduction to Nmap", size="2"),
                            rx.avatar(src="https://www.liquidweb.com/wp-content/uploads/2024/03/nmap-logo-256x256-1.avif", size="4")
                        ),
                        rx.markdown("First let see *`what is nmap?`*"),
                        rx.text("Nmap is a Tool created for scanning a network such as discover hosts, ports and also can be used to detect OS version. The creator is ", rx.link("Gordon Lyon", href="https://en.wikipedia.org/wiki/Gordon_Lyon")
                        ),
                        rx.vstack(
                            rx.heading("Short Cuts", 
                                       size="2",
                                       padding_top=Size.DEFAULT.value),
                            rx.blockquote(rx.code("nmap [scan type] [options] [target]", color_scheme="violet", variant="ghost", high_contrast=True), color_scheme="violet"),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Syntax"),
                                        rx.table.column_header_cell("Example"),
                                        rx.table.column_header_cell("Description")
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.row_header_cell("-p", color=Colors.TEXT),
                                        rx.table.cell("nmap -p 23 127.0.0.0"),
                                        rx.table.cell("Scan specific port")
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell("-p [range]", color=Colors.TEXT),
                                        rx.table.cell("nmap -p 23-445 127.0.0"),
                                        rx.table.cell("Scan a range of ports")
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell("-p-", color=Colors.TEXT),
                                        rx.table.cell("nmap -p- 127.0.0.0"),
                                        rx.table.cell("Scan all ports")
                                    ),
                                )
                            ),
                        align="center"
                        ),
                        width="355px",
                    )
            ),

    )
