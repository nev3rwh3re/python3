import sys
import time
import struct
import os


for c in range(0,0xff):
    #r.replace('\n',' ').replace('\r', '')
    print(repr(c))
    print("#"*24)
    payload = 'A' * c
    print("payload: {}".format(payload))

for c in range(0,0xff+1):
    #r.replace('\n',' ').replace('\r', '')
    print(repr(c))
    print("#"*24)
    payload = chr(c)
    print("payload: {} ({})".format(hex(c),chr(c)))

