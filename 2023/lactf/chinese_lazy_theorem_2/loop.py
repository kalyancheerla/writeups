#!/usr/bin/env python3

from pwn import *

import warnings
warnings.filterwarnings("ignore")

HOST = 'lac.tf'
PORT = 31111

conn = remote(HOST, PORT)

p = int(conn.readline().decode('utf-8').strip('\n'))
q = int(conn.readline().decode('utf-8').strip('\n'))

#cal X1 & X2
X1 = pow(q, -1, p)
X2 = pow(p, -1, q)

conn.writelineafter(">> ", b'1')
conn.writelineafter("Type your modulus here: ", str(p))

r1= int(conn.readline().decode('utf-8').strip('\n'))

conn.writelineafter(">> ", b'1')
conn.writelineafter("Type your modulus here: ", str(q))

r2= int(conn.readline().decode('utf-8').strip('\n'))

conn.writelineafter(">> ", b'2')
x = (r1*q*X1+r2*p*X2)%(p*q)

for i in range(30):
    conn.writelineafter("Type your guess here: ", str(x))
    print(conn.readline().decode('utf-8').strip('\n'))
    x+=p*q
