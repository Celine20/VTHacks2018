#!/usr/bin/env python3
import argparse
import socket
import sys
#import tkinter
#from tkinter import *

#need to create a gui that sends which purchases the customer wants
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMessage(s, msg):
    #do encryption here
    s.send(msg.encode('ascii'))

def recieveMessage(s, size):
    msg = s.recv(size)
    #do decryption here
    return msg

def buttonPushed():
    print("Ordered Coffee")

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
        sys.exit()

    host = userInfo.n
    port = int(userInfo.p)
    size = int(userInfo.s)

    #Add call to functions here
    '''try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket creation failed with error: %s" %(err))
        sys.exit()'''

    print("socket created!")

    try:
        s.connect((host, port))
        #msg = s.recv(1024)
        msg = recieveMessage(s, size)
        #s.close() #take out
        print("Message recieved: " + msg.decode('ascii'))


    except Exception as ex:
        print("Connection Failed: " + str(ex))


    msg = "ACCT:1234:ITEM:COFFEE:PRICE:2.50"
    #s.send(msg.encode('ascii'))
    sendMessage(s, msg)

    msg2 = "end"
    #s.send(msg2.encode('ascii'))
    sendMessage(s, msg2)
    #AFTER SENDING END....ALWAYS WAIT TO RECIEVE ONE LAST Message
    msg = recieveMessage(s, size)
    print("Message recieved: \n" + msg.decode('ascii'))

    s.close()

    return;

main()
