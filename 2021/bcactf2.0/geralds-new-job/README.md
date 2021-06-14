# Gerald's New Job
**Category :** forensic

## Description
Being a secret agent didn't exactly work out for Gerald. He's been training to become a translator for dinosaurs going on vacation, and he just got his traslator's licence. But when he sees it, it doesn't seem to belong to him... can you help him find his licence?

## Solution
Use binwalk to extract the contents of the pdf and look for GeraldFlag.png.

```
# extract the contents in the pdf file
$ binwalk -e gerald.pdf
# view it in a image viewer
$ eog _gerald.pdf.extracted/GeraldFlag.png
```

## Flag
bcactf{g3ra1d_15_a_ma5ter_p01yg1ot_0769348}
