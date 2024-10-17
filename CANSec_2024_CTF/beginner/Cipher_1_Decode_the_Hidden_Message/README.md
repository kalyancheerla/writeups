# Cipher 1: Decode the Hidden Message
**Points**: 25

## Description
You've been provided with a file named decode\_cipher\_1.txt containing 10 examples of plaintext and ciphertext. Your goal is to identify the encryption pattern and decrypt the final ciphertext to reveal the flag. The ciphertext for the flag is located at the end of the file and is as follows: nemktlxvnkxyetzpbmavhfiexqbmr. Your task is to decrypt this ciphertext and submit the flag in all lowercase. Can you uncover the hidden message?

## Writeup
Here, we can clearly see both the plaintext and ciphertext were given.
```
Plaintext: Plant a tree
Ciphertext: Ietgm t mkxx

```
After looking at it, we can observe that the characters are of equal length, and same letters had same cipher letters and capital letters have capital cipher letters. My first thoughts were then it would be a ROT Cipher (Caesar cipher).

```
A B C D E F G H I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

So, to find the ROT number we can just assume the letters as numbers and subtract them.
```
P-I = 16-9 = 7
l-e = 12-5 = 7
a-t = 1-20 = -19 mod26 = 7
n-g = 14-7 = 7
t-m = 20-13 = 7
a-t = 7
t-m = 7
r-k = 18-11 = 7
e-x = 5-24 = -19 mod26 = 7
e-x = 7
```
As, we had checked it for all the characters too which resulted in same ROT7. We can clearly confirm this as a ROT cipher. Now, lets get the Flag.

```
 n  e  m  k  t  l  x  v  n  k  x  y  e  t  z  p  b  m  a  v  h  f  i  e  x  q  b  m  r
14  5 13 11 20 12 24 22 14 11 24 25  5 20 26 16  2 13  1 22  8  6  9  5 24 17  2 13 18
 7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7
--------------------------------------------------------------------------------------
21 12 20 18  1 19  5  3 21 18  5  6 12  1  7 23  9 20  8  3 15 13 16 12  5 24  9 20 25
 u  l  t  r  a  s  e  c  u  r  e  f  l  a  g  w  i  t  h  c  o  m  p  l  e  x  i  t  y
--------------------------------------------------------------------------------------
```
By simply adding 7, we can decode the flag as below.

# Flag
ultrasecureflagwithcomplexity
