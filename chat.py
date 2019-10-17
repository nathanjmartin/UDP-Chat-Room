import socket
import sys

name = raw_input("Please enter your chatroom name: ")
print('Welcome to the chatroom, ' + name)

# UDP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 10000

# Try to let user type message and send through the socket
while True:
        # send data
        message = raw_input(name + ": ")
        socket.sendto(message, (udp_ip, udp_port))

        # receive data
        response, address = socket.recvfrom(4096)
        print('User1: ' + str(response))