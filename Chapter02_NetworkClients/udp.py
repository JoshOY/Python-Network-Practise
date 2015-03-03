#!/usr/bin/env python
# -*- coding: utf-8 -*-

# UDP Example - Chapter 2 - udp.py

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

if __name__ == '__main__':
    # Notice that we use socket.SOCK_DGRAM instead of socket.STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(textport)
    except ValueError:
        # That didn't work. Look it uop instead
        port = socket.getservbyname(textport, 'udp')

    s.connect((host, port))
    print("Enter data to transmit: ")
    data = sys.stdin.readline().strip()
    s.sendall(data)
    print("Looking for replies; press Ctrl-C to stop.")
    
    while True:
        buf = s.recv(2048)
        if len(buf) == 0:
            break
        sys.stdout.write(buf)
