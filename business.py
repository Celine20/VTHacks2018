import os
import sys
import socket
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help="Include a port that both are using")
    parser.add_argument('-s', help="Include a shared size for the socket")
    userInfo = parser.parse_args()

    if userInfo.p == None or userInfo.s == None:
        print("Please use the format: ")
        print("customer.py -p [port] -s [size]")
        print("EXAMPLE: customer.py -p 555 -s 1024")
        sys.exit()

    port = int(userInfo.p)
    size = int(userInfo.s)
    host = socket.gethostname()

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind((host, port))
    except socket.error as msg:
        print("Bind failed. Error Message: " + str(msg[0]))
        sys.exit()

    print("Socket connected!")

    #hardcoding backlog
    serversocket.listen(10)
    print("Listening.....")

    while True:

        clientsocket, address = serversocket.accept()
        print("Connected with: " + str(address[0]))

        #data = clientsocket.recv()
        msg = 'Hello, Please send any orders to me!'
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()

        while True:

            data = serversocket.recv()

            if data:
                #call process data
            else if data == "end":
                clientsocket.close()
                print("closed connection with customer")

    return;

main()
