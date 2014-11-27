import socket
import threading
from sys import exit
#import atexit
 

name = raw_input("What is your name?")
 
k = "Q*aDfWa"
 
s = socket.socket()
 
#s.connect(("72.68.144.133",9000))
s.connect(("localhost",9000))

def ec(s,key):
    output = []
    while len(key) < len(s):
        key += key
    for i in range(len(s)):
        output.append(ord(s[i])+ord(key[i]))
        output[i] = chr(output[i])
    output = "".join(output)
    return output
 
def dc(s, key):
    output = []
    while len(key) < len(s):
        key += key
    for i in range(len(s)):
        output.append(ord(s[i])-ord(key[i]))
        output[i] = chr(output[i])
    output = "".join(output)
    return output
 
def getData():
    while True:
        m = s.recv(1024)
        print dc(m, k) # recieves
 
def sendMessages():
    while True:
        m = raw_input("")
        if m == "!@logout":
            closeConnection()
            return
        #print "\033[A                             \033[A"
        s.sendall(ec(name+": "+m, k)) # sends

def closeConnection():
    print "yo"
    s.sendall("!@logout")
 
newData = threading.Thread(target=getData)
send = threading.Thread(target=sendMessages)
newData.start()
send.start()

