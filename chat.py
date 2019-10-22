import socket
import threading

# GUI stuff probably up here


# UDP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 12000

def send_message(message):
        socket.sendto(message.encode('utf-8'), (udp_ip, udp_port))

def receive_message():
        while True:
                response, address = socket.recvfrom(4096)
                message = response.decode("utf-8", "ignore")
                print(message)


if __name__ == "__main__":
    # Not sure about this threading stuff
    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()

    name = input("Enter your chatroom name: ")
    while True:
            message = input(name + ": ")
            message = name + ": " + message
            send_message(message)
            receive_message()