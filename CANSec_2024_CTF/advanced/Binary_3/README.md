# Binary 3: Decode the Compiled Binary
**Points**: 75

## Description
You've been provided with a binary file named `find_me_3`, which is the output of a C program compiled using gcc. Your task is to analyze the binary file and uncover the hidden flag. Use your knowledge to extract the flag from the compiled output. Once you find the hidden message, submit the flag (the flag is case sensitive). Can you reveal the flag?

Note: You can run `./find_me_3 <flag_value>` in order to test if you have gotten the correct flag or not.

## Writeup
Here also, we were given with a ELF64 binary which can even test the flag. So, lets use gdb to find any interesting functions and we can see functions like strcmp(), malloc(), free() and puts(). If my guess was right, the data is getting added into heap using malloc, so lets break at strcmp and find the strings that are being compared. And we can immediately find our flag over there.
```gdb
$ gdb ./find_me_3
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x00000000000010a0  __cxa_finalize@plt
0x00000000000010b0  free@plt
0x00000000000010c0  puts@plt
0x00000000000010d0  __stack_chk_fail@plt
0x00000000000010e0  strcmp@plt
0x00000000000010f0  __stpcpy_chk@plt
0x0000000000001100  malloc@plt
0x0000000000001110  __printf_chk@plt
(gdb) b *strcmp@plt
No symbol table is loaded.  Use the "file" command.
(gdb) b strcmp@plt
Breakpoint 1 at 0x10e0
(gdb) r
Starting program: find_me_3
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
THIS IS FOR TESTING YOUR FLAG - Usage: find_me_3 <secret_code>
[Inferior 1 (process 22219) exited with code 01]
(gdb) r 1
Starting program: find_me_3 1
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Testing the flag...

Breakpoint 1, 0x00005555555550e0 in strcmp@plt ()
(gdb) x/s $rsi
0x5555555592a0: "A5v4NC8DrEv4R9E"
(gdb) x/s $rdi
0x7fffffffebd8: "1"
```

Note:
* I have also used online decompilers to understand the code much better.

# Flag
A5v4NC8DrEv4R9E
