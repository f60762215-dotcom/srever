import random
import subprocess
import os
import socket
# ) # ( #
srever_ip = "100.78.36.104"
srever_port = 5000
start = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start.connect((srever_ip, srever_port))

start.send("m".encode('utf-8'))
answer = start.recv(1024).decode('utf-8')
print(f"new qustaion ~>>> {answer}")
op = int(input("answer ~:>"))
start.send(f"{op}".encode('utf-8'))
answer = start.recv(1024).decode('utf-8')
print(answer)