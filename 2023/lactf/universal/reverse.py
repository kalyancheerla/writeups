#!/usr/bin/env python3

flag='lactf{'+31*'.'+'}'
#0, 1, 2, 3, 4, 5, 37

print(flag, len(flag))
flag = list(flag)

alpha='abcdefghijklmnopqrstuvwxyz01234567890_'

#operations
for i in alpha:
    if ((ord(i) ^ ord(flag[3]) * 7 ^ ~ord(flag[1]) + 13) & 0xFF) == 0xD8:
        flag[26] = i

    if ((ord(i) ^ ord(flag[2]) * 7 ^ ~ord(flag[4]) + 13) & 0xFF) == 0x67:
        flag[36] = i

    if ((ord(i) ^ ord(flag[2]) * 7 ^ ~ord(flag[1]) + 13) & 0xFF) == 0x2F:
        flag[20] = i

for i in alpha:
    if ((ord(flag[36]) ^ ord(i) * 7 ^ ~ord(flag[4]) + 13) & 0xFF) == 0x4B:
        flag[16] = i

    if ((ord(flag[20]) ^ ord(flag[0]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0x65:
        flag[21] = i

    if ((ord(flag[20]) ^ ord(flag[5]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0xC1:
        flag[12] = i

for i in alpha:
    if ((ord(flag[37]) ^ ord(i) * 7 ^ ~ord(flag[21]) + 13) & 0xFF) == 0xDF:
        flag[10] = i

    if ((ord(flag[12]) ^ ord(i) * 7 ^ ~ord(flag[36]) + 13) & 0xFF) == 0x97:
        flag[28] = i

for i in alpha:
    if ((ord(i) ^ ord(flag[10]) * 7 ^ ~ord(flag[20]) + 13) & 0xFF) == 0xBC:
        flag[15] = i

    if ((ord(i) ^ ord(flag[3]) * 7 ^ ~ord(flag[10]) + 13) & 0xFF) == 0xD6:
        flag[8] = i

    if ((ord(flag[26]) ^ ord(flag[10]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0xCB:
        flag[30] = i

    if ((ord(i) ^ ord(flag[28]) * 7 ^ ~ord(flag[37]) + 13) & 0xFF) == 0xBD:
        flag[19] = i

for i in alpha:
    if ((ord(i) ^ ord(flag[19]) * 7 ^ ~ord(flag[1]) + 13) & 0xFF) == 0x6B:
        flag[25] = i

    if ((ord(i) ^ ord(flag[2]) * 7 ^ ~ord(flag[19]) + 13) & 0xFF) == 0x2C:
        flag[35] = i

    if ((ord(flag[19]) ^ ord(i) * 7 ^ ~ord(flag[20]) + 13) & 0xFF) == 0xF6:
        flag[34] = i

for i in alpha:
    if ((ord(flag[25]) ^ ord(i) * 7 ^ ~ord(flag[35]) + 13) & 0xFF) == 0x92:
        flag[27] = i

    if ((ord(flag[35]) ^ ord(flag[4]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0x54:
        flag[33] = i

    if ((ord(flag[34]) ^ ord(i) * 7 ^ ~ord(flag[35]) + 13) & 0xFF) == 0x54:
        flag[22] = i

    if ((ord(flag[3]) ^ ord(flag[35]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0xCD:
        flag[9] = i

    if ((ord(flag[34]) ^ ord(i) * 7 ^ ~ord(flag[36]) + 13) & 0xFF) == 0xB6:
        flag[23] = i

for i in alpha:
    if ((ord(flag[27]) ^ ord(i) * 7 ^ ~ord(flag[9]) + 13) & 0xFF) == 0x36:
        flag[18] = i

    if ((ord(flag[3]) ^ ord(i) * 7 ^ ~ord(flag[22]) + 13) & 0xFF) == 0x20:
        flag[29] = i

    if ((ord(flag[22]) ^ ord(flag[16]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0x6C:
        flag[13] = i

    if ((ord(flag[16]) ^ ord(flag[10]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0xFA:
        flag[14] = i

    if ((ord(flag[1]) ^ ord(flag[33]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0x21:
        flag[31] = i

    if ((ord(flag[4]) ^ ord(i) * 7 ^ ~ord(flag[22]) + 13) & 0xFF) == 0xE3:
        flag[32] = i

for i in alpha:
    if ((ord(flag[12]) ^ ord(i) * 7 ^ ~ord(flag[18]) + 13) & 0xFF) == 0xA5:
        flag[6] = i

    if ((ord(i) ^ ord(flag[4]) * 7 ^ ~ord(flag[13]) + 13) & 0xFF) == 0x63:
        flag[24] = i

    if ((ord(flag[22]) ^ ord(i) * 7 ^ ~ord(flag[29]) + 13) & 0xFF) == 0x55:
        flag[7] = i

for i in alpha:
    if ((ord(flag[24]) ^ ord(flag[9]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0xB9:
        flag[17] = i

    if ((ord(flag[24]) ^ ord(flag[23]) * 7 ^ ~ord(i) + 13) & 0xFF) == 0xCD:
        flag[19] = i

    if ((ord(flag[33]) ^ ord(i) * 7 ^ ~ord(flag[3]) + 13) & 0xFF) == 0xEB:
        flag[11] = i



print(''.join(flag), len(flag))

