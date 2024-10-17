# Binary 2: Decode the Compiled Binary
**Points**: 50

## Description
You've been provided with a binary file named find\_me\_2, which is the output of a C program compiled using gcc. Your task is to analyze the binary file and uncover the hidden flag. Use your knowledge to extract the flag from the compiled output. Once you find the hidden message, submit the flag. Can you reveal the flag?

## Writeup
Given a binary, lets check the binary.
```
$ file ./find_me_2
find_me_2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d5d3548e44f0f1d169e615c58f9a5627fffd79fd, for GNU/Linux 3.2.0, not stripped
```

So, a ELF64 linux binary, lets use gdb to find anything interesting.
```gdb
$ gdb ./find_me_2
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001040  __cxa_finalize@plt
0x0000000000001050  __stack_chk_fail@plt
0x0000000000001060  _start
0x0000000000001090  deregister_tm_clones
0x00000000000010c0  register_tm_clones
0x0000000000001100  __do_global_dtors_aux
0x0000000000001140  frame_dummy
0x0000000000001149  store_flag
0x0000000000001197  main
0x00000000000011b0  _fini
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001197 <+0>:     endbr64
   0x000000000000119b <+4>:     push   rbp
   0x000000000000119c <+5>:     mov    rbp,rsp
   0x000000000000119f <+8>:     mov    eax,0x0
   0x00000000000011a4 <+13>:    call   0x1149 <store_flag>
   0x00000000000011a9 <+18>:    mov    eax,0x0
   0x00000000000011ae <+23>:    pop    rbp
   0x00000000000011af <+24>:    ret
End of assembler dump.
(gdb) disassemble store_flag
Dump of assembler code for function store_flag:
   0x0000000000001149 <+0>:     endbr64
   0x000000000000114d <+4>:     push   rbp
   0x000000000000114e <+5>:     mov    rbp,rsp
   0x0000000000001151 <+8>:     sub    rsp,0x20
   0x0000000000001155 <+12>:    mov    rax,QWORD PTR fs:0x28
   0x000000000000115e <+21>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000001162 <+25>:    xor    eax,eax
   0x0000000000001164 <+27>:    movabs rax,0x724537655277334e
   0x000000000000116e <+37>:    movabs rdx,0x334c304f43536935
   0x0000000000001178 <+47>:    mov    QWORD PTR [rbp-0x20],rax
   0x000000000000117c <+51>:    mov    QWORD PTR [rbp-0x18],rdx
   0x0000000000001180 <+55>:    nop
   0x0000000000001181 <+56>:    mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000001185 <+60>:    sub    rax,QWORD PTR fs:0x28
   0x000000000000118e <+69>:    je     0x1195 <store_flag+76>
   0x0000000000001190 <+71>:    call   0x1050 <__stack_chk_fail@plt>
   0x0000000000001195 <+76>:    leave
   0x0000000000001196 <+77>:    ret
End of assembler dump.
```

We can see from above that store\_flag() function is present and is interesting which actually takes 2 hard-coded byte arrays into rax and rdx, which getting copied into rbp. So, lets set a break point at `*store_flag+55` and run the binary and look for the hard-coded content.
```gdb
(gdb) break *store_flag+55
Breakpoint 1 at 0x1180
(gdb) r
Starting program: find_me_2
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0000555555555180 in store_flag ()
(gdb) x/s $rbp-0x20
0x7fffffffe770: "N3wRe7Er5iSCO0L3"
```
Yup, thats the flag.

Note:
* We can also use Decompiler Explorer too which makes it even easier.
* strings also gives these values, but also gives extra characters before and after these if they are readable characters like below with `H`.
```
...
PTE1
u+UH
N3wRe7ErH
5iSCO0L3H
:*3$"
...
```

# Flag
N3wRe7Er5iSCO0L3
