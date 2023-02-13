#### crypto/chinese-lazy-theorem-1

Hint: Just understanding the modulus

Solution:
After looking at the code we can say that, we need to figureout target in guess to get the flag.
And target%modulus is the response of option 1.

As % or modulus just returns the remainder when divided. For example,

q ≅ r mod(d) => Here r = remainder, d = divisor, a = quotient

So, if divisor > quotient then remainder = quotient.

Exploit: p\*q (for opt 1) to get the target and then send it in opt 2 as input for out guess to get the flag.

Flag: lactf{too_lazy_to_bound_the_modulus}
