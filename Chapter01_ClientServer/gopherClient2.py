#!/usr/bin/env python
# Simple Gopher Client - Chapter 1
# gopherClient2.py

import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print("Error connecting to server: %s" % e)
        sys.exit(1)
        
    s.sendall(filename + "\r\n")

    while True:
        buf = s.recv(2048)
        if len(buf) == 0:
            break
        sys.stdout.write(buf)