#!/usr/bin/env python3

from pwn import *

HOST="ip address" # fa200762b0bd8087.247ctf.com
PORT=50256        # port number

def calculate(strlist):
    x = int(strlist[5])
    y = int(strlist[7][:-1])
    #op = strlist[6]
    #print(x, y, op)
    add = x + y
    print(x+y)
    return str(add)


conn = remote(HOST, PORT)
print(conn.recvline())
for i in range(500):
    print(conn.recvline())
    given_str=conn.recvline()
    print(given_str.decode().split())
    conn.send(calculate(given_str.decode().split()) + "\r\n")

#while True:
print(conn.recvline())
