#!usr/bin/env python
# Chapter 1 - Download Example - download.py

import urllib, sys

f = urllib.urlopen(sys.argv[1])
while True:
    buf = f.read(2048)
    if len(buf) == 0:
        break
    sys.stdout.write(buf)