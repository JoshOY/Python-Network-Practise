#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Revised Connection Example - Chapter 2 - connect2.py

import socket

if __name__ == "__main__":
    print("Creating socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Done.")

    # python的socket库中包含一个getservbyname()函数，
    # 有两个参数：协议名、端口名
    # 可以自动查询并转换为一个端口号
    print("Looking up port number...")
    port = socket.getservbyname("http", "tcp")
    print("Done.")

    print("Connection to remote host on port %d" % port)
    s.connect(("www.baidu.com", port))
    print("Done.")