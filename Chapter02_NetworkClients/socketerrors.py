#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Error Handling Example - Chapter 2 - socketerrors.py
# try this:
# $ python socketerrors.py www.baidu.com 80 /

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print("Strange error creating socket: %s" % e)
        sys.exit(1)

    # Try parsing it as a numeric port number

    try:
        port = int(textport)
    except ValueError:
        # That didn't work, so it's probably a protocol name.
        # Look it up instead.
        try:
            port = socket.getservbyname(textport, 'tcp')
        except socket.error, e:
            print("Couldn't find your port: %s" % e)
            sys.exit(1)
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error, e:
        print("Connection error: %s" % e)
        sys.exit(1)

    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error, e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while True:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if len(buf) == 0:
            break
        sys.stdout.write(buf)