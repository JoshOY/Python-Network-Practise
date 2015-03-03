#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Information Example - Chapter 2 - connect3.py

import socket

if __name__ == "__main__":
    print("Creating socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Done.")

    print("Looking up port number...")
    port = socket.getservbyname("http", "tcp")
    print("Done.")

    print("Connection to remote host on port %d" % port)
    s.connect(("www.baidu.com", port))
    print("Done.")

    print("Connected from " + s.getsockname()[0] + ':' + str(s.getsockname()[1]))
    print("Connected to "   + s.getpeername()[0] + ':' + str(s.getpeername()[1]))