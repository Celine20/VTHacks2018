import wolframalpha
import re
import binascii


#takes string that is to be converted
def toHex(s):
    s = s.encode('utf-8')
    test = binascii.hexlify(s)
    test = str(test)
    test = test[2:len(test)-1]
    return test;

#takes: "client" or "server", message to write
def encrypt(user, message):
    if(user == "client"):
        readFile = open("clientReadFile.txt","w+") #create a read text file
        #writeFile = open("clientWriteFile.txt","w+") #create a write text file
        otherGB = serverGB
    elif(user == "server"):
        readFile = open("serverReadFile.txt","w+") #create a read text file
        #writeFile = open("serverWriteFile.txt","w+") #create a write text file
        otherGB = clientGB
        
    splitMessage = [message[i:i+4] for i in range(0, len(message), 4)]
    #print(splitMessage)

    #put loop to dump 4block chunks to a file
    for i in range(0, len(splitMessage), 1):
        #writting the x text
        readFile.write("%s\n" %int(toHex(splitMessage[i]), 16))

    readFile.close()

    #print("number of blocks = %d" %len(splitMessage))
    #print("Sending...this may take a moment.")

    readFile = open("%sReadFile.txt" %user,"r") 
    
    if readFile.mode == 'r': #checks to make sure the file is actually open
        output = "" 
        for i in range(0, len(splitMessage), 1):
            #generating a random a for each block
            res = client.query("RandomInteger[{1, %s}]" %p)
            randA = next(res.results).text        
            randA = 23929576152213104632700858091 #REMOVE THIS

            res = client.query("PowerMod[%s,%s,%s]" %(g, randA, p))
            GA = next(res.results).text

            res = client.query("PowerMod[%s,%s,%s]" %(otherGB, randA, p))
            key = next(res.results).text

            x = readFile.readline()
            res = client.query("Mod[%s*%s, %s]" %(key,x,p))
            y = next(res.results).text
            
            #writeFile.write("%s, %s\n" %(GA, y))
            output += "%s, %s\n" %(GA, y)
	        
    #print("Sent: %s" %output)

    readFile.close()
    #writeFile.close()
    return output;

#takes: "client" or "server"
def decrypt(user, message):
    if(user == "client"):
        other = "server"
        userB = clientB
        
    elif(user == "server"):
        other = "client"
        userB = serverB
        
    readFile = open("TEST.txt","w+")
    readFile.write("%s" %message)
    readFile.close()    
    #print("Collecting information...this may take a moment.")

    num_lines = sum(1 for line in open("TEST.txt","r"))
    #print("file has %s lines" %num_lines)
    
    readFile = open("TEST.txt","r") 
    output = ""
    if readFile.mode == 'r': #checks to make sure the file is actually open
        
        for i in range(0, num_lines, 1):
            contents = readFile.readline()
            #print(contents)
            contents = [x.strip() for x in contents.split(',')]
            
            #get first part of 2 part chunk
            GA = contents[0]
            #get second part of 2 part chunk
            y = contents[1]
            
            #calculate key
            res = client.query("PowerMod[%s,%s,%s]" %(GA, userB, p))
            key = next(res.results).text
            
            #gets the inverse
            res = client.query("Mod[PowerMod[%s,-1,%s]*%s, %s]" %(key, p, y, p))
            x = next(res.results).text
            
            temp = hex(int(x))
            output += temp[2:]
    
    #converts the dec output to hex then ascii (fix needed!)
    output = str(output)
    output = bytearray.fromhex(output).decode()
    
    #print(output)           
    #print("Done!")

    readFile.close()
    #writeFile.close()
    
    
    return output;



#changed based on machine
user = "client"
    
phoneBook = open("phoneBook.txt","w+") #create a phoneBook text file

p = 25556559725105479157329017931

g = 3

clientB = 20190429513084307099315842458

serverB = 12360986268816101893709120573


clientGB = 12700962374221636332321133770

serverGB = 11458955528766375362023495100

phoneBook.write("%d\n%d\n%d\n%d\n" % (p, g, clientGB, serverGB))

app_id = "8UHTA8-5QGXGEJ4AT"
client = wolframalpha.Client(app_id)

#message = "test"
#take in input somehow (TBD)
#val = encrypt("client", message)
#decrypt("server", val)




