#!/usr/bin/env python3
import argparse
import socket
import sys
import os
import tkinter
from tkinter import *
import code

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMessage(msg): #(s, msg)
    #do encryption here
    s.send(msg.encode('ascii'))

def recieveMessage(size): #(s, size)
    msg = s.recv(size)
    #do decryption here
    return msg

def sendEndMessage(msg, size):
    s.send(msg.encode('ascii'))
    msg2 = recieveMessage(size)
    decryptedMsg2 = code.decrypt("client", msg2)
    print("Message recieved: \n" + decryptedMsg2.decode('ascii'))

def register(account):
    #x = E1.get()
    print("We recieved your account information")

def order(item, price):
    print("You ordered: " + str(item))
    msg = str(item) + ":" + str(price)
    encryptMsg = code.encrypt("client", msg)
    s.send(encryptMsg.encode('ascii'))

def runGUI(size):
    #start gui
    top = tkinter.Tk()
    top.geometry("400x300")
    label1 = Label(text="Enter Account Here").grid(row=0, column=0)
    v = StringVar()
    E1 = Entry(top, textvariable=v)
    E1.grid(row=0, column=1)
    B1 = Button(text="Register", command=lambda: register(E1.get())).grid(row=0,column=2)
    label2 = Label(text="~Our Menu~").grid(row=3, column=1)
    label3 = Label(text="Coffee").grid(row=4, column=0)
    label4 = Label(text="$2.50").grid(row=4, column=1)
    B2 = Button(text="Order", command = lambda: order("Cofeee", 2.50)).grid(row=4, column=2)
    label5 = Label(text="Latte").grid(row=5, column=0)
    label6 = Label(text="$3.50").grid(row=5, column=1)
    B3 = Button(text="Order", command = lambda: order("Latte", 3.50)).grid(row=5, column=2)
    label7 = Label(text="Mocha").grid(row=6, column=0)
    label8 = Label(text="$3.00").grid(row=6, column=1)
    B4 = Button(text="Order", command = lambda: order("Mocha", 3.00)).grid(row=6, column=2)
    label9 = Label(text="Muffin").grid(row=7, column=0)
    label10 = Label(text="$1.50").grid(row=7, column=1)
    B5 = Button(text="Order", command = lambda: order("Muffin", 1.50)).grid(row=7, column=2)
    label11 = Label(text="Donut").grid(row=8, column=0)
    label12 = Label(text="$1.00").grid(row=8, column=1)
    B6 = Button(text="Order", command = lambda: order("Donut", 1.00)).grid(row=8, column=2)
    B7 = Button(text="Get Check", command = lambda: sendEndMessage("end", size)).grid(row=9,column=1)
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
        print("EXAMPLE: [do not use sudo] python3 customer.py -n 127.0.0.1 -p 555 -s 1024")
        sys.exit()

    host = userInfo.n
    port = int(userInfo.p)
    size = int(userInfo.s)

    #made global ... should have done a class
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

    runGUI(size)

    s.close()

    return;

main()
