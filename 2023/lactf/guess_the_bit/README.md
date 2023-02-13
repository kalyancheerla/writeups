### **Title:** crypto/guess-the-bit!

**Hint:** Count 6 power.

**Solution:**\
From the code, we can see that c is multiplied with 6 only when bit is set.\
So, if we find 6 power in c as odd we can conclude the guess bit as set else not.

As we have to iterate over 150 times guessing our guess bit, a pwntools script like in here will help.

**Exploit:** ./loop.py

**Flag:** lactf{sm4ll_plalnt3xt_sp4ac3s_ar3n't_al4ways_e4sy}
