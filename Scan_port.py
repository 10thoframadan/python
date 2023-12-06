import socket
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
YELLOW = Fore.YELLOW
RED = Fore.RED

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"{GREEN}[+] Port {port} is open {RESET}")
        else:
            print(f"{GRAY}[!] Port {port} is closed {RESET}", end="\r")
    except Exception as exception:
         print(f"{RED}Exception: {exception} {RESET}", end="\r")

def main():
    host = input(f"{YELLOW}[?] Enter the host: {RESET}")
    for port in range(1, 1025):
        scan_port(host, port)
if __name__ == "__main__":
    main()