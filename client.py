import socket
HOST ='100.78.36.104'
PORT = 5000
srever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srever.connect((HOST, PORT))
command = input("Debian_client~>")
srever.send(command.encode())