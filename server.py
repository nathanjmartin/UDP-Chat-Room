import socket


# UDP Socket, IP, port, binding
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 12000
socket.bind((udp_ip, udp_port))

# list to hold the addresses
addresses = []

while True:
    recv, address = socket.recvfrom(4096)
    print(recv)

    if address in addresses:
        print("")
    else:
        print("New client connected to chatroom ")
        addresses.append(address)
    #Sends back message to each client that has connected
    for client in addresses:
        if recv != "":
            socket.sendto(recv, client)