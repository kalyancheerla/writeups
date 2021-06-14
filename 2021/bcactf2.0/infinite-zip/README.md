# Infinite Zip
**Category :** foren

## Description
Here's a zip, there's a zip. Zip zip everywhere.

## Solution
Provided a multi level zip file.

```
# unzip the file for first time
$ unzip flag.zip
# for loop to unzip the file for multiple times
$ for i in {999..0}; do unzip "{i}.zip"; done
# grep the flag
$ strings flag.png | grep -i bcactf
```

# Flag
bcactf{z1p_1n51d3_4_z1p_4_3v3r}