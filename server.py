import socket


# UDP Socket, IP, port, binding
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 12000
socket.bind((udp_ip, udp_port))

# list to hold the addresses
addresses = []
# list to hold the messages
messages = []
emojis = ["\U0001f600", "\U0001F606", "\U0001F923"]

while True:
    recv, address = socket.recvfrom(4096)
    # grab the sequence number off of recv and save it in a variable
    decoded = str(recv)
    # find first occurence of seq
    seq_index = decoded.find('seq')
    # since seq number is going to be appended to the end of the message,
    # take from the seq_index, to the end of the string
    sequence_number = decoded[seq_index:]

    print(recv)
    print(address)
    print(sequence_number)
    messages.append(recv)

    if address in addresses:
        print("")
    else:
        # HANDSHAKE PROCESS
        # send the ackowledgement of the syn packet if it receives it
        SYNACK = 'SYNACK'
        if 'SYN' in str(recv):
            socket.sendto(SYNACK.encode('utf-8'), address)
        # listen for the acknowledgement
        recv, address = socket.recvfrom(4096)
        if 'ACK' in str(recv):
            print('Handshake completed!')
            print("New client connected to chatroom ")
            addresses.append(address)
    
    # prints out all the client's sent messages if requested
    if 'list_messages' in recv.decode("utf-8", "ignore"):
        msg_notification = 'List of all messages:\n---------------------------------------'
        socket.sendto(msg_notification.encode('utf-8'), address)
        for message in messages:
            socket.sendto(message, address)
    
    if 'file_transfer' in recv.decode("utf-8", "ignore"):
        # receive the file
        buffer = 1024
        data, addr = socket.recvfrom(buffer)
        print('Received file'), data.strip()
        f = open(data.strip(), 'wb')
        
        data, addr = socket.recvfrom(buffer)

        # try writing, and if there is still data, continue writing
        try:
            while(data):
                f.write(data)
                data, addr = socket.recvfrom(buffer)
        except:
            f.close()
            print('File downloaded')

        # SEND FILE TO ALL CLIENTS

        # open the file, read binary
        send_file = open(f, "rb")
        new_data = send_file.read(buffer)


        # send 1024 bytes at a time of the file
        socket.sendto(new_data, (udp_ip, udp_port))

        # while there is still data, continue sending the rest of the file
        while(new_data):
                if(socket.sendto(new_data, (udp_ip, udp_port))):
                        print('Sending file...')
                        new_data = send_file.read(buffer)

    #Sends back message to each client that has connected
    for client in addresses:
        if recv != "" and client != address:
            socket.sendto(recv, client)