import socket
Domain = input("Get Host By Subdomain: ")
Host = socket.gethostbyname(Domain)
print(Host)
