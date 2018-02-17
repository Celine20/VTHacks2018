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

    port = userInfo.p
    size = userInfo.s

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind((socket.gethostname(), port))
    except socket.error as msg:
        print("Bind failed. Error Message: " + str(msg[0]))
        sys.exit()

    print("Socket connected!")

    #hardcoding backlog
    s.listen(10)
    print("Listening.....")

    while True:

        (clientsocket, address) = serversocket.accept()
        print("Connected with: " + str(address[0]))

    serversocket.close()

    return;

main()
