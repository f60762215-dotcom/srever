import socket
import os
import time
SREVER_IP = '100.78.36.104'
PORT = 5000
file = 'user_name_you.txt'
def save_user_name():
    if not os.path.exists(file):
        with open(file, 'w', encoding='utf-8') as filer:
            filer.write(" ")
        with open(file, 'a', encoding='utf-8') as filer:
            print("pls enter your username ")
            user_name = input("user name: ")
            filer.write(user_name + '\n')
    elif os.path.exists(file):
        print("your user_name loaded .1")
save_user_name()
while True:

    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SREVER_IP, PORT))
    with open(file, 'r', encoding='utf-8') as files:
        lines = files.readlines()
    message = input("message: ")
    from_user = lines[0]
    print(from_user)
    full_message = f"user: {from_user}    , message: {message}"
    client_socket.send(full_message.encode('utf-8'))
    time.sleep(2)

    respons = client_socket.recv(1024).decode('utf-8')
    
    if respons:
        
                
        print(f"srever answer: {respons}")
    client_socket.close()