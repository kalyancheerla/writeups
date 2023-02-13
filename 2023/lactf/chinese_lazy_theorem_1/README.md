### **Title:** crypto/chinese-lazy-theorem-1

**Hint:** Just understanding the modulus

**Solution:**\
After looking at the code we can say that, we need to figureout the target in guess to get the flag.
And (target % modulus) is the response of option 1.

As '%' or modulus just returns the remainder when divided. For example,\
a ≅ r mod(d) => Here r = remainder, d = divisor, a = dividend.

So, if divisor > dividend then remainder = dividend.

**Exploit:** p\*q (for opt 1) to get the target and then send it in opt 2 as input guess to get the flag.

**Flag:** lactf{too_lazy_to_bound_the_modulus}
