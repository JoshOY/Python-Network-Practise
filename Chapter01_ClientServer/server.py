#!usr/bin/env python
# Simple Server - Chapter 1 - server.py

import socket, sys

host = ''     # Bind to all interfaces
port = 10086

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)

    print("Server is running on port %d; Press Ctrl-C to terminate." % port)

    while True:
        clientsock, clientaddr = s.accept()
        clientfile = clientsock.makefile('rw', 0)
        clientfile.write("Welcome, " + str(clientaddr) + "\n")
        sys.stdout.write("Receive connection from %s:%s" % (clientaddr[0], clientaddr[1]))
        clientfile.write("Please enter a string: ")
        line = clientfile.readline().strip()        # Remove \n at the end of the string.
        clientfile.write("You entered %d characters.\n" % len(line))
        clientfile.close()
        clientsock.close()