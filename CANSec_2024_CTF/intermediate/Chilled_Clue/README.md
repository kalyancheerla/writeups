# Chilled Clue
**Points**: 50

## Description
The 'cool' cat may look relaxed, but there’s something important hidden inside the image. It’s up to you to discover the secret message. The challenge requires a close examination of the image and a strategic approach to reveal what’s beneath the surface.

## Writeup
Given an PNG image of cat and lying inside is our flag. So, lets check for metadata and hidden files using exiftool, binwalk, and zsteg.
```sh
$ exiftool cool_cat.png
ExifTool Version Number         : 12.76
File Name                       : cool_cat.png
Directory                       : .
File Size                       : 465 kB
File Modification Date/Time     : 2024:10:17 17:30:08-05:00
File Access Date/Time           : 2024:10:21 12:12:40-05:00
File Inode Change Date/Time     : 2024:10:17 17:31:37-05:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 800
Image Height                    : 525
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Seed                            : 6432
Flag Length                     : 24
Image Size                      : 800x525
Megapixels                      : 0.420
```

Output from binwalk and zsteg:
```
$ binwalk cool_cat.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 800 x 525, 8-bit/color RGB, non-interlaced
87            0x57            Zlib compressed data, default compression

$ zsteg cool_cat.png
meta Seed           ..

    00000000: 36 34 33 32                                       |6432            |
meta FlagLength     ..

    00000000: 32 34                                             |24              |
b2,g,lsb,xy         .. file: OpenPGP Secret Key
b2,b,lsb,xy         .. file: OpenPGP Secret Key
b3,r,lsb,xy         .. file: PGP Secret Sub-key -
b3,bgr,lsb,xy       .. file: MySQL table definition file Version 73, MySQL version -1424291009
b4,g,lsb,xy         .. text: "\"\"\"\"33DDDW"
b4,b,lsb,xy         .. text: "\"3DDUUUUVfDDDDUUUUDDDD33\"\"!"
b4,b,msb,xy         .. text: ["w" repeated 8 times]
b4,rgb,lsb,xy       .. text: "!2$2C$2C"
```

The interesting thing we found were Seed 6432 and the length of the flag which is 24. I couldn't determine the seed 6432 being used by the random function like in a python solution provided. But I took that as a hint for my solution, lets think that we were provided with a Hint that the seed is useful to find the randomized pixel positions where the data resides. So, now lets develop a python solution to get the data.

Also, due to this randomization of the flag bits; the signature based finders like binwalk and zsteg couldn't determine anything useful.

The solution, I had developed was a simple python function named `extract_randomized_data_from_red_lsb()` which takes input and seed and generates binary file as output. In here, based on random seed and the random generator, the order of data bits is determined and data is extracted accordingly. We can also modify the functionality to extract the randomized data bits from different planes and bit positions accordingly.

Now, I had used strings and found the flag.
```
$ python extract_randomized_data_from_red_lsb.py cool_cat.png 6432 output
Binary data extracted and saved to: output
$ strings output | head -5
Ve8Y_De8U4E&7eRy_M1nDFU1
KEFq
dRK.
0w"=
|       =5Z
```

The one good thing, this challenge has taught me is something completely different where normal signature based functionalities could easily determine the data if the data bits are stored in proper linear order and randomizing these positions of data bits could easily obfuscate the data from plain sight i.e., from these signature based tools which is quite intriguing.

# Flag
Ve8Y\_De8U4E&7eRy\_M1nDFU1
