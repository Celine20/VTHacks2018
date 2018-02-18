#!/usr/bin/env python3
import os
import sys
import socket
import argparse
import code

class customerBill:
    def __init__(self, accountID):
        self.accountID = accountID
        self.billItems = []
        #self.billPrices = []
        self.total = 0
        self.menuPrices = {'c':2.50, 'l':3.50, 'm':3.00, 'u':1.50, 'd':1.00}
    def addItem(self, item):
        self.billItems.append(item)
        #self.billPrices.append(price)
        self.total += self.menuPrices[item]
    def getFullName(self, item):
        if item == 'c':
            return "Coffee"
        elif item == 'l':
            return "Lattee"
        elif item == 'm':
            return "Mocha"
        elif item == 'u':
            return "Muffin"
        elif item == 'd':
            return "Donut"
    def chargeCustomer(self):
        response = "_______________________________\n" + "       Bill Summary   \n"
        response = response + "_______________________________\n"
        response = response + "Hello Customer!\n" #response = response + "Hello Customer " + str(self.accountID) + "!\n"
        for x in range(0, len(self.billItems)):
            #response = response + "Item: {} || Price: ${}\n".format(self.billItems[x], self.billPrices[x]) #make two decimals if you get around to it
            #response = response + "Item: {} || Price: ${}\n" %self.billItems[x] %self.billPrices[x]
            temp = self.getFullName(self.billItems[x])
            temp2 = self.menuPrices[self.billItems[x]]
            #response = response + "Item: {} || Price: ${}\n".format(temp, temp2)
            response = response + "Item: %s || Price: $%.2f\n" %(temp, temp2)
        response = response + "Total Purchases: $%.2f\n" %self.total
        response = response + "Thank you for shopping with us!"
        response = response +  "\n_______________________________"
        return response

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help="Include a port that both are using")
    parser.add_argument('-s', help="Include a shared size for the socket")
    userInfo = parser.parse_args()

    if userInfo.p == None or userInfo.s == None:
        print("Please use the format: ")
        print("customer.py -p [port] -s [size]")
        print("EXAMPLE: sudo python3 customer.py -p 555 -s 1024")
        sys.exit()

    port = int(userInfo.p)
    size = int(userInfo.s)
    host = '0.0.0.0' #socket.gethostname()

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind((host, port))
    except socket.error as msg:
        print("Bind failed. Error Message: " + str(msg[0]))
        sys.exit()

    #hardcoding backlog
    serversocket.listen(10)
    print("Listening For Customer.....")

    while True:

        clientsocket, address = serversocket.accept()
        print("New customer: " + str(address[0]))

        msg = 'Hello Customer, Please send any orders to me!'
        clientsocket.send(msg.encode('ascii'))

        #make instance of customerBill
        customerName = str(address[0])
        currentCustomer = customerBill(customerName)

        while True:

            data = clientsocket.recv(size)

            if data.decode() == "end":
                bill = currentCustomer.chargeCustomer()
                clientsocket.send(bill.encode('ascii'))
                clientsocket.close()
                print("closed connection with customer: " + str(address[0]))
                break
            elif data:
                #print("process data...." + str(data))
                decodedData = data.decode()
                decryptedData = code.decrypt("server", decodedData)
                temp = decryptedData
                temp2 = self.menuPrices[decryptedData]
                response =  "Item: %s || Price: $%.2f\n" %(temp, temp2)
                currentCustomer.addItem(decryptedData)
                #splitData = decryptedData.split(":")
                #currentCustomer.addItem(splitData[0], float(splitData[1]))
                #make a process data function that stores data

    return;

main()
