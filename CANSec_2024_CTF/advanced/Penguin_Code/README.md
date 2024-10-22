# Penguin Code
**Points**: 75

## Description
This Linux logo holds more than just brand recognition. A message has been hidden within the image, waiting for those who can unlock it. Your objective is to investigate the image carefully and retrieve the hidden content. Use your technical skills wisely to solve the challenge.

## Writeup
These are actually very complicated, and below is the writeup based on solutions produced by event host Mohamed Abdelnaby (credits to him).

First, lets check the image's metadata using exiftool.
```
ExifTool Version Number         : 12.76
File Name                       : linux_logo.png
Directory                       : .
File Size                       : 96 kB
File Modification Date/Time     : 2024:10:17 19:19:28-05:00
File Access Date/Time           : 2024:10:17 19:26:03-05:00
File Inode Change Date/Time     : 2024:10:17 19:20:14-05:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 421
Image Height                    : 500
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Exif Byte Order                 : Big-endian (Motorola, MM)
Software                        : IV: 484b8d6160ebd069738bc38a9939b1e7
Image Size                      : 421x500
Megapixels                      : 0.210
```

Here, we can notice one interesting thing which software metadata which didn't contain software name instead contains IV which could be initialization vector and thats what it is. Now by applying various filters to the image (inversion) we could actually see a password which might be helpful.
```
IV:  484b8d6160ebd069738bc38a9939b1e7
key: PassWord123@
```

Based on IV and key, we can safely assume that this is a AES CBC encryption. But now we need to understand the bits where the data is present and extract them and finally decrypt them to get our flag.

But one issue here is the zsteg analyzes based on known techniques and outputs based on known file signatures and as the data in-here is encrypted, I don't think it can help to identify its signature. Also, the bits of data are stored randomly at different positions using python's random function with a seed and this is something I don't think any steg analysis tools can identify and I also came to know about this based on the solution produced.

So, now I need to write my logic to extract the encrypted data from RED LSB (this can be assumed based on `Chilled_Clue` challenge). So, I had used the same script but with a small tweak of taking the seed Big int produced by a string of SHA256 hash (this I came to know based on the solution produced).

As the data extracted from the RED LSB based on the random seed was still encrypted, we simply cannot use strings to get our data. Now, I had used a openssl AES CBC decryption command to decrypt the data. And also the seed for our random generator was the same password key "PassWord123@" which is also the key for AES CBC encryption.
```
$ python extract_randomized_data_from_red_lsb.py
Usage: python extract_randomized_data_from_red_lsb.py <image_path> <seed> <output_path>

$ python extract_randomized_data_from_red_lsb.py linux_logo.png "PassWord123@" output
Binary data extracted and saved to: output

$ openssl enc -aes-256-cbc -d -in output -out decrypted_output -K $(echo -n 'PassWord123@' | sha256sum | cut -d' ' -f1) -iv 484b8d6160ebd069738bc38a9939b1e7 -nopad
bad decrypt
4027486E24740000:error:1C80006B:Provider routines:ossl_cipher_generic_block_final:wrong final block length:../providers/implementations/ciphers/ciphercommon.c:443:

$ strings decrypted_output | head -5
1tSg1v1nGh1gHK3Ysl4yNoC4pBeT
7y-yKC
k|[:
#b#/
n[p||
```

Here, we can see I had used my custom python function to extract the randomized data and openssl with AES CBC scheme where the key is input as SHA256 Hash with the IV in hex and no-padding. And finally, used strings to get the challenge flag.

# Flag
1tSg1v1nGh1gHK3Ysl4yNoC4pBeT
