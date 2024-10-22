# Credits for this python solution to Mohamed Abdelnaby at OU.
import sys
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from PIL import Image
import hashlib
import numpy as np

# To get the key, zoom into the picture to get it. It's located on the right arm of the linux logo penguin
# To get the IV value, run exiftool <image> to get the meta data of the image

def decrypt_flag(encrypted_flag, key_extracted, iv):

    # The key is easy to get, it's hidden on the arm of the linux logo penguin
    # The IV is also easy to get, it's hidden in the meta data of the image
    # First, hash the extracted key using SHA-256 to generate a 256-bit key
    # We use hashlib's sha256() and then call .digest() to get the binary form of the hash
    key = hashlib.sha256(key_extracted.encode()).digest()

    # You need to try different ciphers, but this one is AES in CBC mode, this step is brute-force step
    # You can create an AES cipher object in CBC mode using the extracted key and the IV
    # We use AES.new() to initialize it with the key, mode CBC, and the IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    try:

        # Decrypt the flag using the AES cipher
        # The result is still padded, so we need to unpad it later
        decrypted_flag = cipher.decrypt(encrypted_flag)

        # Print the decrypted flag in hexadecimal format before removing the padding (This will help you check it)
        print(f"Decrypted flag before unpadding (hex): {decrypted_flag.hex()}")

        # Unpad the decrypted flag to remove the extra padding added during encryption
        unpadded_flag = unpad(decrypted_flag, AES.block_size)

        # Convert the unpadded flag from bytes to string and return it
        return unpadded_flag.decode()

    except ValueError as e:
        # If an error occurs during unpadding (like incorrect padding), print the error and the encrypted flag in hex to help you understand what's wrong
        print(f"Error during unpadding: {e}")
        print(f"Encrypted flag (hex): {encrypted_flag.hex()}")
        raise

    except Exception as e:
        # This is for general uncatched erros
        print(f"General error during decryption: {e}")
        raise

def extract_data_from_lsb(pixels, width, height, num_bits, seed):

    # Use the random seed to initialize the pseudo-random number generator to get deterministic sequence
    random_num_gen = random.Random(seed)

    # You need to calculate the total number of pixels in the image width times height
    num_pixels = width * height

    # Generate a list of pixel positions in the image, then shuffle them based on the seed
    positions = list(range(num_pixels))
    random_num_gen.shuffle(positions)

    data_bits = ''

    # This will get you to extract the flag
    for i in range(num_bits): # num_bits needs to be brute forced - This is another difference between this questions and the previous one
        pos = positions[i] # positions[i] gives the pixel index where the i-th bit of the flag is hidden.
        x = pos % width # (x-axis) position of the pixel in the image
        y = pos // width # (y-axis) position of the pixel in the image

        # This part is tricky, we could have chosen any channel, you could try the blue channel, green channel, and red channel.
        # Also, we chose the LSB of the channel, you could try the MSB for example
        # For this flag, we chose the least significant bit (LSB) of the red channel

        # Since we have calculated the x and y for the position of the pixel in the image, we can use it to get the red channel value, given by index [y, x][0]
        red_channel_LSB = pixels[y, x][0] # You may be wondering why we're using [y,x] instead of [x,y], here, pixels are passed as numpy array
                                          # numpy array is easier for pixel manipulation. You could have used PIL and in that case you'd use pixels[x,y]
                                          # This is another way to show different ways to get the values of the LSB of the red channel

        # red_channel_LSB & 1 is a bitwise operation that extracts the LSB of the red channel value
        # You're storing it as a string value and you're appending it to data_bits
        data_bits += str(red_channel_LSB & 1)

    # Once all bits are extracted, you need to convert the binary string into bytes
    # You need bytes to get tthe bytes this time to use it to decrypt the flag
    # That's another different between this questions and the cool cat question
    data_bytes = bytes(int(data_bits[i:i + 8], 2) for i in range(0, len(data_bits), 8))

    # Return the extracted data as bytes
    return data_bytes

def extract_flag_linux_logo(image_path, extracted_key, iv_hex, expected_flag_length):

    # You need to convert the IV from its hexadecimal representation to bytes - This step is important
    iv = bytes.fromhex(iv_hex)

    # Open the image
    img = Image.open(image_path).convert('RGB')  # Convert the image to RGB mode to read the pixel values
    width, height = img.size  # Get the width and height of the image
    pixels = np.array(img)  # Convert the image to a numpy array (for easier pixel manipulation)


    # This step is difficult, but essentially you need to generate a seed, since you only know the IV and Key, you can try each of them for the seed
    # Generate a seed for the pseudo-random number generator using the hashed password (SHA-256) converted to an integer
    seed = int.from_bytes(hashlib.sha256(extracted_key.encode()).digest(), 'big')

    # You can't find the expected flag length anywhere, so this is a brute force step, but you know that whatever length it is, you'll multiply it by 8
    num_flag_bits = expected_flag_length * 8

    # Extract the flag data from the LSB of the red channel of the image pixels using the seed
    flag_bytes = extract_data_from_lsb(pixels, width, height, num_flag_bits, seed)
    print(f"Extracted flag bytes (hex): {flag_bytes.hex()}")

    # Decrypt the flag using the decrypted bytes
    decrypted_flag = decrypt_flag(flag_bytes, extracted_key, iv)

    # Print the extracted flag
    print(f"Extracted flag: {decrypted_flag}")

# You can use this function from the command line
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python extract_flag_linux_logo.py <stego_image> <password> <iv_hex> <expected_flag_length>")
        sys.exit(1)

    image_path = sys.argv[1]  # Path to the image
    extracted_key = sys.argv[2]  # The key to decrypt the flag
    iv_hex = sys.argv[3]  # IV value you got from the meta data
    expected_flag_length = int(sys.argv[4])  # Length of the flag (This is not given, so you need to guess, the correct length is 28 but you need to enter 32
                                             # this is meant to be brute forced)

    # Extract the flag and decrypt it
    extract_flag_linux_logo(image_path, extracted_key, iv_hex, expected_flag_length)


# Command Line "python extract_flag_linux_logo.py linux_logo.png 'PassWord123@' '484b8d6160ebd069738bc38a9939b1e7' 32"

