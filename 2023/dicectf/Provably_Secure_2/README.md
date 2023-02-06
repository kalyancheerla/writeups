##### Hint: Just figureout the xor from the challenge code. Don't go down the rabbit hole of doing decryption or encryption separately.
\
This challenge changes the code a little from the Provably Secure challenge where previous cipher texts cannot be used for immediate decrypting.

So, to figureout the `m_bit` -- it doesn't change during immediate encryptions (when pk1 and pk2 stays same) and decryptions. Also the challenge code only checks for full cipher text.

##### Encrypt function outline:
* Input:     msg
* Output:  256bytes hash of random + 256bytes hash of (msg ⊕ random)

##### Decrypt Function outline:
* Input: 512bytes hash
* Output: random ⊕ (msg ⊕ random) = msg

So, lets do 2 immediate encryptions with 4 msgs then we will have 2 cipher texts. \
`Cipher text 1 = random1 256B hash + ((m1|m2) ⊕ random1) 256B hash` \
`Cipher text 2 = random2 256B hash + ((m3|m4) ⊕ random2) 256B hash` \
\
Now, lets do 2 decryptions for new cipher texts as below by interchaning the 256 blocks of cipher text 1 and cipher text 2 to escape the comparison check. \
`new cipher text 1 = random1 256B hash + ((m3|m4) ⊕ random2) 256B hash` \
`new cipher text 2 = random2 256B hash + ((m1|m2) ⊕ random1) 256B hash` \
\
Outputs will be like below, \
`Output1 = random1 ⊕ (m3|m4) ⊕ random2` \
`Output2 = random2 ⊕ (m1|m2) ⊕ random1` \
\
XOR the outputs to eliminate the randoms, \
`Ouput1 ⊕ Ouput2 = (m3|m4) ⊕ (m1|m2)` \
\
Finally, now we can figureout the `m_bit` from the msgs xor.

Find the python script in here which does the same but for 128 times.
