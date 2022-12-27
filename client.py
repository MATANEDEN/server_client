import socket

MAX_MSG_LEGTH = 1024
SERVER_PORT = 1730
SERVER_IP = "127.0.0.1"


def main():
    print("setting up server....")
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((SERVER_IP, SERVER_PORT))
    data = my_socket.recv(MAX_MSG_LEGTH).decode('utf-8')
    print(data)

    while True:
        message = input("print message or EXIT to finish")
        my_socket.send(message.encode('utf-8'))
        client_data = my_socket.recv(MAX_MSG_LEGTH).decode()
        print("Server send back " + client_data)
        if message == "EXIT":
            break
    my_socket.close()


main()
