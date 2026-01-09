import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def check_username(username):
    url = f"https://www.instagram.com/{username}/"

    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        html = r.text.lower()

        # Active account
        if '"profilepage_' in html or 'followers' in html:
            return "ACTIVE"

        # Previously used / disabled
        if "sorry, this page isn't available" in html and "instagram" in html:
            return "NOT_AVAILABLE"

        # Fully free
        if "sorry, this page isn't available" in html:
            return "AVAILABLE"

        return "UNKNOWN"

    except requests.exceptions.RequestException:
        return "ERROR"

def main():
    print(Fore.CYAN + "Instagram Username Status Checker")
    print(Fore.CYAN + "-" * 45)

    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            usernames = [u.strip() for u in f if u.strip()]
    except FileNotFoundError:
        print(Fore.RED + "user.txt file পাওয়া যায়নি")
        input("\nPress Enter to exit...")
        return

    for username in usernames:
        status = check_username(username)

        if status == "ACTIVE":
            print(Fore.GREEN + f"{username} -> ACTIVE")
        elif status == "AVAILABLE":
            print(Fore.CYAN + f"{username} -> AVAILABLE")
        elif status == "NOT_AVAILABLE":
            print(Fore.RED + f"{username} -> NOT AVAILABLE (Used Before / Disabled)")
        else:
            print(Fore.YELLOW + f"{username} -> {status}")

        time.sleep(5.5)  # Delay555

    print(Style.BRIGHT + "\nCheck complete")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
