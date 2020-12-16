# Izzy
**category :** reverse,
**points :** 66,
**solves :** 77.

## Description :
Izzy was writing a novel based on Mayan culture. Will Tom finish her book so that she could rest in peace?

## Solution :
There are 2 files in here,
1. A script - command.sh<n/>.
```
$ cat command.sh 
#!/bin/bash
export i=99; grep -o . <<< cat flag.txt| while read letter;  do i=$((i+1)); printf '%02x'  "$(($(python3 -c "import os;import decimal; import time; decimal.getcontext().prec = 2992; index=int(os.environ.get('i')); x = str(decimal.Decimal(1) / decimal.Decimal((1010 - int(time.strftime('%m')))*1000 +1))[2:]; print(int(x[3*index:3*index+3]))") ^ $(printf '%#x\n' '"'$letter)))">>result.txt; done;
```
2. A text file - result.txt.
```
$ cat result.txt
2855140337590c3434040c5b411346492b3113430c11254a49220a17b3def0b3b0e1f2b7d7bdfdb8
```

We can understand from the script that characters from flag.txt were XOR'ed with certain numbers and the final hex values were printted in result.txt. From the result.txt we can also deduce that flag will be of 40 chars (since 80 hex chars).

A xor B = A⊕B => B = A xor (A⊕B)

So logically, feeding the binary output of result.txt to the same script logic should provide the hex values of flag.
Okay lets do it. (take result.txt as backup)
```
$ xxd -r -p result.txt > flag.txt; mv result.txt result_old.txt
$ ./command.sh
$ xxd -r -p result.txt
L0rd_0f_Xib41b4:_De4th_15_iX
```
We got a flag but if we count the chars, it doesn't tally to 40 chars. This is because of grep not getting all the chars in our flag.txt file where some special chars were present.

So to get the complete flag, below is a simple python script I had written which mostly contains the same python logic from the command.sh<n/> script.
```
$ cat inverse.py
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
```
Output :
```
$ ./inverse.py 
L0rd_0f_Xib41b4:_De4th_15_th3_r04dt0_4w3
```

# Flag :
ASIS{L0rd_0f_Xib41b4:_De4th_15_th3_r04dt0_4w3}

