import reflex as rx
from enum import Enum

BASE_STYLE={
        rx.heading: {
            "fontFamily": "'Press Start 2P', sans-serif",
        },
        rx.text: {
            "fontFamily" : "Expletus Sans"
        }
    }

NAVBAR = {
        "bg" : "rgba(230, 23, 157, 0.15)",
        "backdrop-filter" : "blur(8px)"
    }

NAVBAR2 = {
        "bg" : "rgba(230, 23, 157, 0.15)",
        "backdrop-filter" : "blur(8px)",
        "border_radius" : "50px"
    }
# Fonts
class Fonts(Enum):
    UBU = "Ubuntu Condensed"
    EXPLETUS = "Expletus Sans"
    ICE = "Poppins-Light"
    PRESS = "'Press Start 2P', sans-serif"
# Constants
class Colors(Enum):
    BACK = "rgba(230, 23, 157, 0.15)"
    TEXT = " #E384FF"
    ICONS = "#865DFF"
    BLACK = "#0e0d0d"
    ORANGE = "#FF7518"

# IMAGENES
LOGO = "https://avatars.githubusercontent.com/u/125932914?s=96&v=4"

COFFEE = "https://imgs.search.brave.com/OVSYJrPMTvlN74s7udBZ8JfiyIrVWky5k0-MT7QCUdk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jbGlw/YXJ0LWxpYnJhcnku/Y29tL2ltZy83NDY3/OTIucG5n"

AVATAR = "https://imgs.search.brave.com/hBxaEQ4iEgTNPkb1dbE33YN57AJcW6DW_nDea027Fw4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtd2l4bXAtZWQz/MGE4NmI4YzRjYTg4/Nzc3MzU5NGMyLndp/eG1wLmNvbS9mLzYx/ZDhmNzNhLTNkZDYt/NGExNy1iNmY3LTg1/NGNmOGNiZjFjMS9k/ZWt2NHFnLTU4M2Zh/NGZiLWFjZjgtNGY0/ZC05OGU0LThhNGE5/NWJjMWQxMi5wbmcv/djEvZmlsbC93XzEy/ODAsaF8xNTU4L3N1/a3VuYV9wbmdfYnlf/ZmFyc3MxX2Rla3Y0/cWctZnVsbHZpZXcu/cG5nP3Rva2VuPWV5/SjBlWEFpT2lKS1Yx/UWlMQ0poYkdjaU9p/SklVekkxTmlKOS5l/eUp6ZFdJaU9pSjFj/bTQ2WVhCd09qZGxN/R1F4T0RnNU9ESXlO/alF6TnpOaE5XWXda/RFF4TldWaE1HUXlO/bVV3SWl3aWFYTnpJ/am9pZFhKdU9tRndj/RG8zWlRCa01UZzRP/VGd5TWpZME16Y3pZ/VFZtTUdRME1UVmxZ/VEJrTWpabE1DSXNJ/bTlpYWlJNlcxdDdJ/bWhsYVdkb2RDSTZJ/anc5TVRVMU9DSXNJ/bkJoZEdnaU9pSmNM/MlpjTHpZeFpEaG1O/ek5oTFROa1pEWXRO/R0V4TnkxaU5tWTNM/VGcxTkdObU9HTmla/akZqTVZ3dlpHVnJk/alJ4WnkwMU9ETm1Z/VFJtWWkxaFkyWTRM/VFJtTkdRdE9UaGxO/QzA0WVRSaE9UVmlZ/ekZrTVRJdWNHNW5J/aXdpZDJsa2RHZ2lP/aUk4UFRFeU9EQWlm/VjFkTENKaGRXUWlP/bHNpZFhKdU9uTmxj/blpwWTJVNmFXMWha/MlV1YjNCbGNtRjBh/Vzl1Y3lKZGZRLkJn/enhaX1pUc0x0VGpN/VXZKUm4xWS12RTRK/cUgxXzYzM0hDUG0t/a3J4UDg"

## Languages

BASH = "https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/Bash-Dark.svg"

CPP = "https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/CPP.svg"

PYTHON = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Python-Dark.svg"

HTML = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/HTML.svg"

CSS = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/CSS.svg"

MD = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Markdown-Dark.svg"

GIT = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Git.svg"

GITHUBLOGO = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Github-Dark.svg"

NEOVIM = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/NeoVim-Dark.svg"

OBSIDIAN = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Obsidian-Dark.svg"

POWERSHELL = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Powershell-Dark.svg"

VSCODE = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/VSCode-Dark.svg"

WINDOWS = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Windows-Dark.svg"

UBUNTU = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Ubuntu-Dark.svg"

KALI = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Kali-Dark.svg"

DEBIAN = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Debian-Dark.svg"

LINUX = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Linux-Dark.svg"

PHOTOSHOP = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Photoshop.svg"

REGEX = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Regex-Dark.svg"

WORDPRESS = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Wordpress.svg"

AMAZON = "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/AWS-Dark.svg"

## SOCIAL MEDIA
GITHUB = "https://github.com/viepaix"
TWITCH = "https://www.twitch.tv/viepaix"
INSTAGRAM = "https://www.instagram.com/viepaix_/"
YOUTUBE = "https://www.youtube.com/@v1epaix"
KICK = "https://kick.com/viepaix"
PAYPAL = "https://www.paypal.com/paypalme/viepaix23"

# Sizes

class Size(Enum):
    SMALLER = ".25em"
    SMALL = ".5em"
    DEFAULT = "1em"
    MEDIUM = "3.5em"
    BIGGER = "5em"
    BIGEST = "7.5em"
    BLOGACC = "12em"
# MouseOver

class MouseOver(rx.State):
    heading_text: str = "0x560x58"

    def on_mouse_enter(self):
        self.heading_text = "ｼ Santiago"

    def on_mouse_leave(self):
        self.heading_text = "0x560x58"



