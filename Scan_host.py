import socket

def scan_host():
  name = input("Enter the Host address: ")
  host = socket.gethostbyname(name)
  print(host)

scan_host()
