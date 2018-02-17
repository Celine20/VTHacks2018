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

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print(socket.gethostname())
    #print(socket.gethostbyaddr("127.0.0.1"))
    try:
        serversocket.bind(("0.0.0.0", port)) #((socket.gethostname(), port)) #hardcode on pi
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
        msg = 'blah'
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()


    return;

main()
