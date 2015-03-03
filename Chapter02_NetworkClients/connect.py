#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic Connection Example - Chapter 2 - connect.py

import socket

if __name__ == '__main__':
    print("Creating socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Done.")

    print("Connecting to remote host...")
    s.connect(("www.baidu.com", 80))
    print("Done.")