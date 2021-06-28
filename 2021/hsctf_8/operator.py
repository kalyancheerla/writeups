#!/usr/bin/env python3

import sys
from pwn import *

HOST = 'not-really-math.hsc.tf'
PORT = 1337

def operator(given_str):
    new_str = '((' + given_str.replace('a', '+').replace('m', ')*(') + ')) % (2**32 - 1)'
    return str(eval(new_str))

conn = remote(HOST, PORT)
print(conn.recvline())
given_str = conn.recvline()
print(given_str.decode('utf-8'))
conn.send(operator(given_str.decode('utf-8').replace('\n', '')) + "\n")

for i in range(11):
    given_str = conn.recvline()
    print(given_str.decode('utf-8'))
    conn.send(operator(given_str.decode('utf-8').replace('\n', '')[2:]) + "\n")

#while True:
print(conn.recvline())
