# Create a server socket which listens for connections.
# Once a connection is established it saves the data into
# a txt file. It then reads and decodes from base64. 

import socket
import base64      

#---Open a new connection---#
port = 50000                    
s = socket.socket() # Create the socket object as s             
host = "" # Get local machine name
s.bind((host, port)) # Bind to the port
s.listen(5) # Wait for client connection.

print('Server listening....')

#---Establish connection with client---#
while True:
    conn, addr = s.accept()   
    print('Got connection from', addr)

    while True:
        #---Receive data---#
        data = conn.recv(1024)

        if not data:
            break
        
        
        #---Fix b' padding error---#
        new = str(data)
        new2 = new[2:]
        if "'" in new2:
            removed = new2.replace("'", "")
            with open("D:/work/work2/work3/Networking/SocketSend/somedata.txt", "a") as writedata:
                writedata.write(removed)
                writedata.close()
        
        #---Recreate the file---#
        readdata = open("D:/work/work2/work3/Networking/SocketSend/somedata.txt", "r").read()
        fh = open('imageToSave.jpeg', 'wb')
        fh.write(base64.b64decode(readdata)) # Decoding happens here
        fh.close()
        
    print('Data Received')
    break

conn.close()