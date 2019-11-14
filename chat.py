import socket
import threading
import time

# GUI stuff probably up here


# UDP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 12000

# go-back-N to resend any lost data
# I'd like my timeout to be 5 seconds
def reliable_message_transfer(message):
        sequence_number = 'seq123'
        # add the sequence number to the message
        message = message + str(sequence_number)

        # code for sending the packet here
        socket.sendto(message.encode('utf-8'), (udp_ip, udp_port))

        # start the timer
        start_time = time.time()
       
        # code for receiving packet here
        msg, address = socket.recvfrom(4096)

        end_time = time.time()
        # code for resending the message if there is a timeout or not the correct ack is received
        if (end_time - start_time >= 5) or 'ACK' + str(sequence_number) not in msg: # OR ACK + sequence_number not in msg
                socket.sendto(message.encode('utf-8'), (udp_ip, udp_port))


# NEED TO IMPLEMENT SEQUENCE NUMBERS ON THIS STILL
def file_transfer(file_name):
        buffer = 1024
        # open the file, read binary
        f = open(file_name, "rb")
        data = f.read(buffer)

        # send 1024 bytes at a time of the file
        socket.sendto(data, (udp_ip, udp_port))

        # while there is still data, continue sending the rest of the file
        while(data):
                if(socket.sendto(data, (udp_ip, udp_port))):
                        print('Sending file...')
                        data = f.read(buffer)

# Receiving the file from the server
def file_receive(file_name):
        pass

# Handshake to establish a connection
def handshake():
        SYN = 'SYN_packet'
        ACK = 'ACK_packet'
        # need to send a packet with the sequence number, & if the server responds with the correct ack w/ the same seq number, send the message
        socket.sendto(SYN.encode('utf-8'), (udp_ip, udp_port))

        # grab the response
        response, address = socket.recvfrom(4096)

        # check if the response is a SYNACK packet
        if 'SYNACK' in str(response):
                socket.sendto(ACK.encode('utf-8'), (udp_ip, udp_port))
                print('Handshake completed!')


def send_message(message):
        socket.sendto(message.encode('utf-8'), (udp_ip, udp_port))

def receive_message():
        while True:
                response, address = socket.recvfrom(4096)
                message = response.decode("utf-8", "ignore")
                print(message)

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive_message)
    # perform a handshake between the client & server
    handshake()

    # prompt user for name
    name = input("Enter your chatroom name: ")
    print('-----------------------------------------------------------------------------')
    send_message(name + " connected to the chatroom!")
    print('Type list_messages to see all of your messages! ')
    print(name + " connected to the chatroom!")
    # start the receive messages thread
    receive_thread.start()
    while True:
            message = input("")
            message = name + ": " + message
            send_message(message)