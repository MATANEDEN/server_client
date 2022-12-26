import socket

MAX_MSG_LEGTH = 1024
SERVER_PORT = 1730
SERVER_IP = "127.0.0.1"


def main():
    print("setting up server....")
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((SERVER_IP, SERVER_PORT))
    connection = my_socket.recv(MAX_MSG_LEGTH).decode('utf-8')
    print(connection)

    while True:
        message = input("print message")
        my_socket.send(message.encode('utf-8'))
        data = my_socket.recv(MAX_MSG_LEGTH).decode()
        print(data)
    my_socket.close()


main()