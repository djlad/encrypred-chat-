import socket
import threading


def ec(s, key):
    output = []
    while len(key) < len(s):
        key += key
    for i in range(len(s)):
        output.append(ord(s[i])+ord(key[i]))
        output[i] = chr(output[i])
    output = "".join(output)
    return output
 
def dc(s, key):
    # print s
    output = []
    while len(key) < len(s):
        key += key
    for i in range(len(s)):
        output.append(ord(s[i])-ord(key[i]))
        output[i] = chr(output[i])
    output = "".join(output)
    return output
 
 
s = socket.socket()
 
s.bind(("",9000))
s.listen(3)
clients = []
 
 
def getClients():
    while True:
        clients.append(s.accept())
        clients[len(clients)-1][0].setblocking(0)#make socket nonblocking
 
        print clients[len(clients)-1][1] # print address

def getMessages():
    while True:
        for client in clients:
            try:
                mes = client[0].recv(1024)
                if mes == "!@logout":
                    print "client exited"
                    clients.remove(client)
                    break
                else:
                    for i in clients:
                        i[0].sendall(mes) # send messages*
            except:
                pass
 
newClients = threading.Thread(target=getClients)
messages = threading.Thread(target=getMessages)
 
newClients.start()
messages.start()