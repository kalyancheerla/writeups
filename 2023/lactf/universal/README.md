### **Title:** rev/universal

**Hint:** A smart bruteforcer to figure-out flag chars

**Solution:**\
I used online tools for decompiling the java class file and saved it in the FlagChecker.java

From the code we can deduce that, flag is 38 chars length and
each char byte is used in some binary operations.

Also, we can assume that the flag starts with 'lactf{' and ends with '}' and
contains alphanum with underscore as characters.

As, we know 0-5 and 37 indices of the flag. We can go ahead and find the conditionals
where we can plug and deduce other chars.

So, by using these new obtained chars we can determine other chars in the same way.

Please find the full code for the solution in [here](reverse.py).

**Exploit:** ./reverse.py

**Flag:** `lactf{1_d0nt_see_3_b1ll10n_s0lv3s_y3t}`
