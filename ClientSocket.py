#!/usr/bin/env python3

import socket
import base64

HEADERSIZE = 10

#---open file and encode---#
with open('/root/Documents/Coding/picture.jpeg', 'rb') as imageFile: # Example directory path
    x = base64.b64encode(imageFile.read())

#---establish connection---#
s = socket.socket()             
host = "" # IP of the server 
port = 50000                   
s.connect((host, port))

#---send file---#
s.send(x)
s.shutdown(socket.SHUT_WR)
print('Successfully sent the file')
s.close()

print('connection closed')