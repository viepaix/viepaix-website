import reflex as rx

from mysite.styles.styles import *

def nmapShortCuts() -> rx.Component:
    return rx.box(
        rx.desktop_only(
                rx.vstack(
                    rx.vstack(
                        rx.heading("Short Cuts", 
                                    size="2",
                                    padding_top=Size.MEDIUM.value),
                            rx.blockquote(rx.code("nmap [scan type] [options] [target]", color_scheme="violet", variant="ghost", high_contrast=True), color_scheme="violet"),
                            align="center"
                        ),
                        rx.hstack(
                            rx.card(
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
                                        rx.table.row(
                                            rx.table.row_header_cell("-sn", color=Colors.TEXT),
                                            rx.table.cell("nmap -sn 127.0.0.0"),
                                            rx.table.cell("Disable port scan, usefull for scan devices inside a network.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-Pn", color=Colors.TEXT),
                                            rx.table.cell("nmap -Pn 127.0.0.0/24"),
                                            rx.table.cell("Theat the hosts as online. (work good with the -sn option)")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-F", color=Colors.TEXT),
                                            rx.table.cell("nmap -F 127.0.0.0"),
                                            rx.table.cell("Fewer ports will be scanned, it will be faster")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-r", color=Colors.TEXT),
                                            rx.table.cell("nmap -r -p- 127.0.0.0"),
                                            rx.table.cell("The option will scan the ports sequentially, don't randomized.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("--top-ports [number]", color=Colors.TEXT),
                                            rx.table.cell("nmap --top-ports 100 127.0.0.0"),
                                            rx.table.cell("Scan the most common ports (scan how many you insert)")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-O", color=Colors.TEXT),
                                            rx.table.cell("nmap -O 127.0.0.0"),
                                            rx.table.cell("This will enable the OS detection (not 100% precise)")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-sU", color=Colors.TEXT),
                                            rx.table.cell("nmap -sU 127.0.0.0"),
                                            rx.table.cell("Scan with UDP protocol")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-sV", color=Colors.TEXT),
                                            rx.table.cell("nmap -sV 127.0.0.0"),
                                            rx.table.cell("This determine the version of the service that is running.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-D", color=Colors.TEXT),
                                            rx.table.cell("nmap -D 127.0.0.0"),
                                            rx.table.cell("Create a decoy/clon of different ips in the scan")
                                        ),
                                    )
                                ),
                            ),
                            width="100%",
                            align="center",
                            padding_bottom=Size.DEFAULT
                            ),
                        rx.card(
                            rx.heading("Output Nmap commands and description", size="2", color=Colors.TEXT),
                                rx.table.root(
                                    rx.table.header(
                                        rx.table.row(
                                            rx.table.column_header_cell("Output format"),
                                            rx.table.column_header_cell("example"),
                                            rx.table.column_header_cell("Description"),
                                        )
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.row_header_cell("-oN",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oN nmapOutput"),
                                            rx.table.cell("The output of the scan will be in nmap format")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-oX",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oX xmlOutput"),
                                            rx.table.cell("The output of the scan will be in a XML format, usefull for carry easier.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-oS",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oN scriptOutput"),
                                            rx.table.cell("The output of the scan will be in a scriptible format that could help to hide or make a little difficult to read.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-oG",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oN grepeableOutput"),
                                            rx.table.cell("The output of the scan will be in a grepeable format to use tools to access the port or other information easier.")
                                        ),
                                    )
                            ),
                        ),
                        align="center"
                )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                    rx.vstack(
                        rx.heading("Short Cuts", 
                                    size="2",
                                    padding_top=Size.MEDIUM.value),
                            rx.blockquote(rx.code("nmap [scan type] [options] [target]", color_scheme="violet", variant="ghost", high_contrast=True), color_scheme="violet"),
                            align="center"
                        ),
                        rx.hstack(
                            rx.card(
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
                                        rx.table.row(
                                            rx.table.row_header_cell("-sn", color=Colors.TEXT),
                                            rx.table.cell("nmap -sn 127.0.0.0"),
                                            rx.table.cell("Disable port scan, usefull for scan devices inside a network.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-Pn", color=Colors.TEXT),
                                            rx.table.cell("nmap -Pn 127.0.0.0/24"),
                                            rx.table.cell("Theat the hosts as online. (work good with the -sn option)")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-F", color=Colors.TEXT),
                                            rx.table.cell("nmap -F 127.0.0.0"),
                                            rx.table.cell("Fewer ports will be scanned, it will be faster")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-r", color=Colors.TEXT),
                                            rx.table.cell("nmap -r -p- 127.0.0.0"),
                                            rx.table.cell("The option will scan the ports sequentially, don't randomized.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("--top-ports [number]", color=Colors.TEXT),
                                            rx.table.cell("nmap --top-ports 100 127.0.0.0"),
                                            rx.table.cell("Scan the most common ports (scan how many you insert)")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-O", color=Colors.TEXT),
                                            rx.table.cell("nmap -O 127.0.0.0"),
                                            rx.table.cell("This will enable the OS detection (not 100% precise)")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-sU", color=Colors.TEXT),
                                            rx.table.cell("nmap -sU 127.0.0.0"),
                                            rx.table.cell("Scan with UDP protocol")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-sV", color=Colors.TEXT),
                                            rx.table.cell("nmap -sV 127.0.0.0"),
                                            rx.table.cell("This determine the version of the service that is running.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-D", color=Colors.TEXT),
                                            rx.table.cell("nmap -D 127.0.0.0"),
                                            rx.table.cell("Create a decoy/clon of different ips in the scan")
                                        ),
                                    )
                                ),
                            ),
                            align="center",
                            padding_bottom=Size.DEFAULT
                            ),
                        rx.card(
                            rx.heading("Output Nmap commands and description", size="2", color=Colors.TEXT),
                                rx.table.root(
                                    rx.table.header(
                                        rx.table.row(
                                            rx.table.column_header_cell("Output format"),
                                            rx.table.column_header_cell("example"),
                                            rx.table.column_header_cell("Description"),
                                        )
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.row_header_cell("-oN",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oN nmapOutput"),
                                            rx.table.cell("The output of the scan will be in nmap format")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-oX",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oX xmlOutput"),
                                            rx.table.cell("The output of the scan will be in a XML format, usefull for carry easier.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-oS",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oN scriptOutput"),
                                            rx.table.cell("The output of the scan will be in a scriptible format that could help to hide or make a little difficult to read.")
                                        ),
                                        rx.table.row(
                                            rx.table.row_header_cell("-oG",color=Colors.ORANGE),
                                            rx.table.cell("nmap -sSV --min-rate 6000 127.0.0.0 -oN grepeableOutput"),
                                            rx.table.cell("The output of the scan will be in a grepeable format to use tools to access the port or other information easier.")
                                        ),
                                    )
                            ),
                        ),
                        align="center",
                        width=Size.PHONE.value
                ),
       )
    )

text1 = "Nmap is a Tool created for scanning a network such as discover hosts, ports and also can be used to detect OS version. The creator is "

text2 = "This tool is one of the main for Pentester, usefull in the first steps in 'hacker' job with the enumeration, footprinting and scanning process. We can create a map of an entire network, discovering devices, open ports, versions and some other information that could be used later in the explotation phase."

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
                        rx.text(text1, rx.link("Gordon Lyon", href="https://en.wikipedia.org/wiki/Gordon_Lyon"),
                        rx.heading("Why nmap?", size="3", padding_top=Size.DEFAULT.value),
                        rx.text(text2)
                        ),
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
                    rx.text(text1, rx.link("Gordon Lyon", href="https://en.wikipedia.org/wiki/Gordon_Lyon"),
                    rx.heading("Why nmap?", size="1", padding_top=Size.DEFAULT),
                    rx.text(text2)
                    ),
                width=Size.PHONE.value,
            )
        )
    )
