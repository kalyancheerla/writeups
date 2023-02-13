#!/usr/bin/env python3

from pwn import *

import warnings
warnings.filterwarnings("ignore")

HOST = 'lac.tf'
PORT = 31190

p = remote(HOST, PORT)

n = p.readline().decode('utf-8').strip('\n').strip('n = ')
n = int(n)
a = p.readline().decode('utf-8').strip('\n').strip('a = ')
a = int(a)

#print(80*'+')
#print(n, a)
#print(80*'+')

def factors6(n):
    count = 0
    if n%2==0 and n%3==0:
        count+=1
        n = n//6
        count+=factors6(n)
    return count

for i in range(150):
    c = p.readline().decode('utf-8').strip('\n').strip('c = ')
    print(80*'+')
    print(c)
    count = factors6(int(c))
    if count%2 == 1:
        guess_bit = 1
    else:
        guess_bit = 0
    print(guess_bit, count)
    print(80*'+')
    p.writelineafter("What is your guess? ", str(guess_bit))

print(p.read())
