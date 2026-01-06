import socket
SREVER_IP = '100.78.36.104'
PORT = 5000

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SREVER_IP, PORT))

message = input("message: ")
from_user = input("user: ")
full_message = f"user: {from_user}    , message: {message}"
client_socket.send(full_message.encode('utf-8'))


respons = client_socket.recv(1024).decode('utf-8')

print(f"srever answer: {respons}")

client_socket.close()