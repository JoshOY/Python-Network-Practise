#!/usr/bin/env python
# Simple Gopher Client with file-like interface - Chapter 1
# gopherClient3.py

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
        
    fd = s.makefile('rw', 0)
    fd.write(filename + "\r\n")

    # Just output the content like reading a file
    for line in fd.readlines():
    	sys.stdout.write(line)