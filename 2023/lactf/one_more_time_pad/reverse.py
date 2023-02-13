#!/usr/bin/env python3

from itertools import cycle
pt = b"Long ago, the four nations lived together in harmony ..."

#key = cycle(b"lactf{??????????????}")
ct = '200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e'
ct = bytes.fromhex(ct).decode('utf-8')

pt = cycle(pt)

#ct = ""
key=""

for cti in ct: #range(len(pt)):
    key += chr(ord(cti) ^ next(pt))
    #b = (pt[i] ^ next(key))
    #ct += f'{b:02x}'
print("key =", key)

#ct = 200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e
