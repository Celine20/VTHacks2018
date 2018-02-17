import argparse
import socket
import sys
import os

def main():
    #Get user input
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="Include a host name for the business")
    parser.add_argument('-p', help="Include a port that both are using")
    parser.add_argument('-s', help="Include a shared size for the socket")
    userInfo = parser.parse_args()

    if userInfo.n == None or userInfo.p == None or userInfo.s == None:
        print("Please use the format: ")
        print("customer.py -n [hostname] -p [port] -s [size]")
        print("EXAMPLE: customer.py -n 127.0.0.1 -p 555 -s 1024")
    else:
        host = userInfo.n
        port = userInfo.p
        size = userInfo.s

    #Add call to functions here
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket creation failed with error: %s" %(err))
        sys.exit()

    s.connect((host, port))

    #get/send data etc.

    s.close()

    return;
