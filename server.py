import socket

MAX_MSG_LEGTH = 1024
SERVER_PORT = 1730
SERVER_IP = "127.0.0.1"
NUMBER_OF_CLIENTS_TO_LISTEN = 1

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(NUMBER_OF_CLIENTS_TO_LISTEN)

    print('before client connect')
    client_socket, address = server_socket.accept()
    print('after client connect')
    client_socket.send('client connected'.encode('utf-8'))

    while True:
        server_data = client_socket.recv(MAX_MSG_LEGTH).decode('utf-8')
        client_socket.send(server_data.encode('utf-8'))
        print('server recv ' + server_data)

    client_socket.close()
    server_socket.close()


main()

