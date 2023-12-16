import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed", end="\r")
        s.close()
    except Exception as e:
        print(e)

def main():
    host = input("Enter the host: ")
    for port in range(1, 1025):
        scan_port(host, port)

if __name__ == "__main__":
    main()
