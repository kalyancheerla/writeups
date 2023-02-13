import java.nio.charset.Charset;
import java.util.Scanner;

class FlagChecker
{
    public static void main(final String[] array) {
        System.out.print("What's the flag? ");
        System.out.flush();
        final Scanner scanner = new Scanner(System.in);
        final String nextLine = scanner.nextLine();
        scanner.close();
        final byte[] flag = nextLine.getBytes(Charset.forName("UTF-8"));
        if (flag.length == 38 &&
((flag[34] ^ flag[23] * 7 ^ ~flag[36] + 13) & 0xFF) == 0xB6 &&
((flag[37] ^ flag[10] * 7 ^ ~flag[21] + 13) & 0xFF) == 0xDF &&
((flag[24] ^ flag[23] * 7 ^ ~flag[19] + 13) & 0xFF) == 0xCD &&
((flag[25] ^ flag[13] * 7 ^ ~flag[23] + 13) & 0xFF) == 0x90 &&
((flag[6] ^ flag[27] * 7 ^ ~flag[25] + 13) & 0xFF) == 0x8A &&
((flag[4] ^ flag[32] * 7 ^ ~flag[22] + 13) & 0xFF) == 0xE3 &&
((flag[25] ^ flag[19] * 7 ^ ~flag[1] + 13) & 0xFF) == 0x6B &&
((flag[22] ^ flag[7] * 7 ^ ~flag[29] + 13) & 0xFF) == 0x55 &&
((flag[15] ^ flag[10] * 7 ^ ~flag[20] + 13) & 0xFF) == 0xBC &&
((flag[29] ^ flag[16] * 7 ^ ~flag[12] + 13) & 0xFF) == 0x58 &&
((flag[35] ^ flag[4] * 7 ^ ~flag[33] + 13) & 0xFF) == 0x54 &&
((flag[36] ^ flag[2] * 7 ^ ~flag[4] + 13) & 0xFF) == 0x67 &&
((flag[26] ^ flag[3] * 7 ^ ~flag[1] + 13) & 0xFF) == 0xD8 &&
((flag[12] ^ flag[6] * 7 ^ ~flag[18] + 13) & 0xFF) == 0xA5 &&
((flag[12] ^ flag[28] * 7 ^ ~flag[36] + 13) & 0xFF) == 0x97 &&
((flag[20] ^ flag[0] * 7 ^ ~flag[21] + 13) & 0xFF) == 0x65 &&
((flag[27] ^ flag[36] * 7 ^ ~flag[14] + 13) & 0xFF) == 0xF8 &&
((flag[35] ^ flag[2] * 7 ^ ~flag[19] + 13) & 0xFF) == 0x2C &&
((flag[13] ^ flag[11] * 7 ^ ~flag[33] + 13) & 0xFF) == 0xF2 &&
((flag[33] ^ flag[11] * 7 ^ ~flag[3] + 13) & 0xFF) == 0xEB &&
((flag[31] ^ flag[37] * 7 ^ ~flag[29] + 13) & 0xFF) == 0xF8 &&
((flag[1] ^ flag[33] * 7 ^ ~flag[31] + 13) & 0xFF) == 0x21 &&
((flag[34] ^ flag[22] * 7 ^ ~flag[35] + 13) & 0xFF) == 0x54 &&
((flag[36] ^ flag[16] * 7 ^ ~flag[4] + 13) & 0xFF) == 0x4B &&
((flag[8] ^ flag[3] * 7 ^ ~flag[10] + 13) & 0xFF) == 0xD6 &&
((flag[20] ^ flag[5] * 7 ^ ~flag[12] + 13) & 0xFF) == 0xC1 &&
((flag[28] ^ flag[34] * 7 ^ ~flag[16] + 13) & 0xFF) == 0xD2 &&
((flag[3] ^ flag[35] * 7 ^ ~flag[9] + 13) & 0xFF) == 0xCD &&
((flag[27] ^ flag[22] * 7 ^ ~flag[2] + 13) & 0xFF) == 0x2E &&
((flag[27] ^ flag[18] * 7 ^ ~flag[9] + 13) & 0xFF) == 0x36 &&
((flag[3] ^ flag[29] * 7 ^ ~flag[22] + 13) & 0xFF) == 0x20 &&
((flag[24] ^ flag[4] * 7 ^ ~flag[13] + 13) & 0xFF) == 0x63 &&
((flag[22] ^ flag[16] * 7 ^ ~flag[13] + 13) & 0xFF) == 0x6C &&
((flag[12] ^ flag[8] * 7 ^ ~flag[30] + 13) & 0xFF) == 0x75 &&
((flag[25] ^ flag[27] * 7 ^ ~flag[35] + 13) & 0xFF) == 0x92 &&
((flag[16] ^ flag[10] * 7 ^ ~flag[14] + 13) & 0xFF) == 0xFA &&
((flag[21] ^ flag[25] * 7 ^ ~flag[12] + 13) & 0xFF) == 0xC3 &&
((flag[26] ^ flag[10] * 7 ^ ~flag[30] + 13) & 0xFF) == 0xCB &&
((flag[20] ^ flag[2] * 7 ^ ~flag[1] + 13) & 0xFF) == 0x2F &&
((flag[34] ^ flag[12] * 7 ^ ~flag[27] + 13) & 0xFF) == 0x79 &&
((flag[19] ^ flag[34] * 7 ^ ~flag[20] + 13) & 0xFF) == 0xF6 &&
((flag[25] ^ flag[22] * 7 ^ ~flag[14] + 13) & 0xFF) == 0x3D &&
((flag[19] ^ flag[28] * 7 ^ ~flag[37] + 13) & 0xFF) == 0xBD &&
((flag[24] ^ flag[9] * 7 ^ ~flag[17] + 13) & 0xFF) == 0xB9) {
            System.out.println("Correct!");
        }
        else {
            System.out.println("Not quite...");
        }
    }
}
