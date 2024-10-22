import gmpy2

# Given values
n = 150000000355000000133
e = 65537
ciphertext = 145844668068067239154

# Factor n to get p and q (Use a factorization tool to get p and q)
p = 15000000007 # Example p
q = 10000000019 # Example q

# Calculate φ(n)
phi_n = (p - 1) * (q - 1)

# Calculate d (modular inverse of e mod φ(n))
d = gmpy2.invert(e, phi_n)

# Decrypt the ciphertext
plaintext = pow(ciphertext, d, n)

# Convert the plaintext number to a string
plaintext_str = str(plaintext)

print("Decrypted message:", plaintext_str)

