import socket
import random_number_generator

def server():
    # create a server socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to port 5500
    serversocket.bind(('', 5500))

    #  become a server socket an queue as much as 5 connect request
    serversocket.listen(5)
    print("Server listening...")

    while True:
         # accept connections from outside
        (connection, address) = serversocket.accept()
        print('Connection with ' + str(address))
        randomint = str(random_number_generator.randomint()) + '\n'

        # Send message
        connection.send(randomint.encode())

        # Close connection
        connection.close()

if __name__ == '__main__':
    server()