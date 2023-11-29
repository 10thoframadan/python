import socket

def scan_host():
  name = input("Enter the domain name: ")
  host = socket.gethostbyname(name)
  print(host)

scan_host()
