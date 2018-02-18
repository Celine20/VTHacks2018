#!/usr/bin/env python3
import argparse
import socket
import sys
import os
import tkinter
from tkinter import *

#need to create a gui that sends which purchases the customer wants
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMessage(msg): #(s, msg)
    #do encryption here
    s.send(msg.encode('ascii'))

def recieveMessage(size): #(s, size)
    msg = s.recv(size)
    #do decryption here
    return msg

def runGUI():
    #start gui
    print("in function...")
    top = tkinter.Tk()
    print("made gui window")
    top.geometry("300x300")
    #frame = LabelFrame(top, text = "Our Menu")
    #label.pack(fill="both", expand="yes")
    print("starting main loop")
    top.mainloop()

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

    print("getting ready to run gui")
    runGUI()
    print("exited gui")
    
    #made global
    '''try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket creation failed with error: %s" %(err))
        sys.exit()'''

    try:
        s.connect((host, port))
        msg = recieveMessage(size)
        print("Message recieved: " + msg.decode('ascii'))
    except Exception as ex:
        print("Connection Failed: " + str(ex))


    '''msg = "ACCT:1234:ITEM:COFFEE:PRICE:2.50"
    #s.send(msg.encode('ascii'))
    sendMessage(msg)

    msg2 = "end"
    #s.send(msg2.encode('ascii'))
    sendMessage(msg2)
    #AFTER SENDING END....ALWAYS WAIT TO RECIEVE ONE LAST Message
    msg = recieveMessage(size)
    print("Message recieved: \n" + msg.decode('ascii'))'''
    #print("getting ready to run gui")
    #runGUI()
    #print("exited gui")
    s.close()

    return;

main()
