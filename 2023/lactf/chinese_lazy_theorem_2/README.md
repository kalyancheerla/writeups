### **Title:** crypto/chinese-lazy-theorem-2

**Hint:** Understand Chinese remainder theorem and use it in here.

**Solution:**\
As we have 2 chances to request modulus of target.

Get remainder, `r1 = target % p`\
and `r2 = target % q`

And as gcd(p,q) = 1. Since p,q are primes.\
we can estimate our target as `(r1*(N/p)*X1 + r2*(N/q)*X2) mod(p*q)`\
where `N = p*q` and `X1 = inverse(N/p) modulo p` and `X2 = inverse(N/q) modulo q`

As target would have multiple values, we can iterate as `target+=N`. (30 guesses)

**Exploit:** ./loop.py

**Flag:** lactf{n0t_$o_l@a@AzY_aNYmORe}
