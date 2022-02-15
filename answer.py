wordlist = ['a,b']
text = []
from calendar import c
from encodings import utf_8
import socket
import random
from typing import Text



server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.connect(('192.168.1.1', 11111))

while(True):
    w1 = random.choice(wordlist)
    w2 = random.choice(wordlist)
    w3 = random.choice(wordlist)
    t = '{}-{}-{}' .format(w1,w2,w3)
    
    server.send(t.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server: ', data_server)
    
server.close()    
    