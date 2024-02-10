import requests
import socket
import sys
import colorama
import time

colorama.init()
KIRMIZI = colorama.Fore.RED
YESIL = colorama.Fore.GREEN
SARI = colorama.Fore.YELLOW
RESET = colorama.Style.RESET_ALL

def animate_text(text, speed=0.02):
    """Animates text from left to right."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_ip_location(ip):
    """Sends an HTTP request to get location information from an IP address."""
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{KIRMIZI}Error occurred: {e}{RESET}")
        sys.exit(1)

def print_location_with_colors(location):
    """Prints location information with improved color scheme."""
    animate_text("İnstagram: @luminate.sec\n", 0.01)



    animate_text(f"{YESIL}Hoşgeldiniz...{RESET}")
    animate_text(f"{YESIL}This Tool Developed By: Lum1Nat3...{RESET}")
    animate_text(f"{YESIL}Lütfen ip adresi giriniz...{RESET}")


    ip = input(f"{KIRMIZI}Enter an IP address: {RESET}")

    if not ip:
        ip = socket.gethostbyname(socket.gethostname())

    animate_text(f"{SARI}Fetching location information...{RESET}")
    time.sleep(1)

    location_info = get_ip_location(ip)
    
    animate_text("\n" + "-" * 40)
    for key, value in location_info.items():
        animate_text(f"{YESIL}{key.capitalize()}: {value}{RESET}", speed=0.001)
    animate_text("-" * 40)

if __name__ == "__main__":
    print_location_with_colors({})
