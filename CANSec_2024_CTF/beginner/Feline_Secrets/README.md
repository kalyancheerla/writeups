# Feline Secrets
**Points**: 25

## Description
At first glance, this picture of a cute cat seems harmless, but there’s more to it than meets the eye. Your task is to analyze the image and uncover a hidden message concealed within. The key lies in careful observation and the use of the right tools.

## Writeup
Given a picture of cat, so I checked the filetype using file and started looking at it with binwalk to find for hidden files.
```
$ file cute_cat_picture.png
cute_cat_picture.png: PNG image data, 1280 x 853, 8-bit/color RGB, non-interlaced
$ binwalk cute_cat_picture.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1280 x 853, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, default compression
1431762       0x15D8D2        Zip archive data, at least v2.0 to extract, compressed size: 292070, uncompressed size: 297670, name: flag.mp3
1723976       0x1A4E48        End of Zip archive, footer length: 22
```

We can immediately see that there is a Zip archive with flag.mp3 file. Lets extract the file and check its contents.
```
$ binwalk -e cute_cat_picture.png  # produces a dir with extracted files
$ ls -la _cute_cat_picture.png.extracted/
total 2272
drwxrwxr-x 2 user user    4096 Oct 17 16:01 .
drwxrwxr-x 3 user user    4096 Oct 17 16:01 ..
-rw-rw-r-- 1 user user  292236 Oct 17 16:01 15D8D2.zip
-rw-rw-r-- 1 user user       0 Oct 17 16:01 29
-rw-rw-r-- 1 user user 1723957 Oct 17 16:01 29.zlib
-rw-rw-r-- 1 user user  297670 Sep 25 07:43 flag.mp3
```

By simply using an audio to text converter like `https://www.notta.ai/en/tools/audio-to-text-converter` in-combination with `https://temp-mail.org/` we can get the text as below,

```
You've made it. Congratulations. The flag is H3D4ENM8S51G4232. All letters are capital letters.
```

# Flag
H3D4ENM8S51G4232
