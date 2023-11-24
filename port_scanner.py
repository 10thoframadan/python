import socket

def scan_port(host, port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((host,port))
    if result == 0:
      print(f"Port {port} is open")
    s.close()
  except socket.error:
    print("Couldn't connect host: {host}")
def main():
  host = input("Enter the host ip address: ")
  for port in range(1, 1025):
    scan_port(host, port)
if __name__ == "__main__":
  main()
