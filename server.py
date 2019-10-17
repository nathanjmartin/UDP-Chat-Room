import socket
import sys

name = raw_input("Please enter your chatroom name: ")
print('Welcome to the chatroom, ' + name)

# UDP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 10000

# bind socket to the ip, and port
socket.bind((udp_ip, udp_port))

while True:
    recv, address = socket.recvfrom(4096)
    print('User2: ' + str(recv))
    response = raw_input(name + ": ")
    socket.sendto(response, address)


