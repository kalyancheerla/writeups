### **Title:** crypto/one-more-time-pad

**Hint:** Just a XOR challenge

**Solution:**\
If we look through the code we can see that the cipher text is just a XOR of msg and key.

```
cipher_text(ct) = message(key) XOR cipher_key(pt)

then,
message(key) = cipher_text(ct) XOR cipher_key(pt)
```

Below, [reverse.py](./reverse.py) just does that to get our flag.

**Exploit:** ./reverse.py

**Flag:** `lactf{b4by_h1t_m3_0ne_m0r3_t1m3}`
