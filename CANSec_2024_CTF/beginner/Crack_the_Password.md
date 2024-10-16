# Crack the Password
**points :** 25.

## Description
You have access to a remote host and a binary (credentials below). Run the binary (/home/Dora/FlagSafe), which will require a password to reveal the flag. The password is more than 20 characters long and contains special characters. However, you can still get the flag!

ssh dora@dora.ctf.sooners.us -p 22111 username: dora password: BoomerSooner

## Writeup
After reading, I immediately sshed into the machine to check the binary and execute it.
```
$ ssh dora@dora.ctf.sooners.us -p 22111
> BoomerSooner
```

I immediately found that the files in home directory of Dora can only be accessed by a different user (name I forgot, lets call him Joe). Also, the FlagSafe binary is an SUID binary which can be executed at the level of permissions as Joe.

Also, the binary tries to take password string which is a 20char length which wouldn't be easy to bruteforce either. My first immediate thought was to coredump the binary with a really long string and To my surprise it immediately gave the flag (Unfortunately, I don't have the flag, as the event is closed and even I don't remember the flag value for it).
