import socket
import threading

# GUI stuff probably up here


# UDP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 12000

# go-back-N to resend any lost data
def reliable_message_transfer():
        pass

def reliable_message_receive():
        pass

def file_transfer(file):
        pass

# Handshake to establish a connection
def handshake(seq):
        pass

def send_message(message):
        socket.sendto(message.encode('utf-8'), (udp_ip, udp_port))

def receive_message():
        while True:
                response, address = socket.recvfrom(4096)
                message = response.decode("utf-8", "ignore")
                print(message)

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive_message)
    name = input("Enter your chatroom name: ")
    send_message(name + " connected to the chatroom!")
    print('Type list_messages to see all of your messages! ')
    receive_thread.start()
    while True:
            message = input("")
            message = name + ": " + message
            send_message(message)