import socket


# UDP Socket, IP, port, binding
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 12000
socket.bind((udp_ip, udp_port))

# list to hold the addresses
addresses = []
messages = []

while True:
    recv, address = socket.recvfrom(4096)
    print(recv)
    print(address)
    messages.append(recv)

    if address in addresses:
        print("")
    else:
        print("New client connected to chatroom ")
        addresses.append(address)
    
    # prints out all the client's sent messages if requested
    if 'list_messages' in recv.decode("utf-8", "ignore"):
        msg_notification = 'List of all messages:\n---------------------------------------'
        socket.sendto(msg_notification.encode('utf-8'), address)
        for message in messages:
            socket.sendto(message, address)

    #Sends back message to each client that has connected
    for client in addresses:
        if recv != "" and client != address:
            socket.sendto(recv, client)