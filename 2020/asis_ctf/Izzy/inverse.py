#!/bin/env python3

import os, decimal, time

decimal.getcontext().prec = 2992
x = str(decimal.Decimal(1) / decimal.Decimal((1010 - int(time.strftime('%m')))*1000 +1))[2:]

index = 99
flag = ""
with open("result.txt", "r") as f:
    while (char := f.read(2)):
        char = bytes.fromhex(char)
        index += 1
        flag += chr(ord(char) ^ int(x[3*index:3*index+3]))

print(flag)
