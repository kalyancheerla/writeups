# Credits for this python solution to Mohamed Abdelnaby (Event Host) at OU.
import sys
import random
from PIL import Image

# To get both the seed and the flag length, run exiftool <image> to get them. They're embedded into the meta data of the image.

def extract_flag_cool_cat(image_path, seed, flag_length):

    # Use Image.open to read an image, we're using .convert("RGB") to read the values in RGB mode (Red, Green, and Blue channels)
    img_cat = Image.open(image_path).convert("RGB")

    # .size will give you the width and the height of the image
    width, height = img_cat.size

    # You need to calculate the total number of pixels for this image, the # of pixels will equal the width of the image times the height of the image
    num_pixels = width * height

    # We're hiding the flag in random pixels of the image, you found the seed, so you can use it to initialize the pseudo-random number generator
    # So what's happening here? The seed will ensure that the sequence of random numbers generated is deterministic
    random.seed(seed)

    # The positions of the pixels will just be a list of the range of the # of pixels you calculated earlier
    # range(num_pixels) is just a sequence from 0 to num_pixels - 1
    positions = list(range(num_pixels))

    # You'll shuffle the positions of the pixels in-place using the seed. This seed was used when embedding the flag, so when we use the same seed to decode it
    # It will return the same order of positions
    random.shuffle(positions)

    # You're given the flag length so you need to calculate the number of bits to extract
    # Each character is 8 bits long (1 byte). So, if the flag is 24 characters, you would extract 24 * 8 = 192 bits.
    bits_to_extract = flag_length * 8
    flag_bits = '' # This will be used when storing the flag bits

    # We need to load the pixel data from the cat image, so use the image_cat.load to do that and store them in pixels
    pixels = img_cat.load()

    # This will get you to extract the flag
    for i in range(bits_to_extract): # You know how long the flag is, so you know how many bits you want to extract so you know when you'll stop extracting
        pos = positions[i] # positions[i] gives the pixel index where the i-th bit of the flag is hidden.
        x = pos % width # (x-axis) position of the pixel in the image
        y = pos // width # (y-axis) position of the pixel in the image

        # This part is tricky, we could have chosen any channel, you could try the blue channel, green channel, and red channel.
        # Also, we chose the LSB of the channel, you could try the MSB for example
        # For this flag, we chose the least significant bit (LSB) of the red channel

        # Since we have calculated the x and y for the position of the pixel in the image, we can use it to get the red channel, red channel is given by index [x,y][0]
        red_channel_LSB = pixels[x, y][0]

        # red_channel_LSB & 1 is a bitwise operation that extracts the LSB of the red channel value
        # You're storing it as a string value and you're appending it to flag_bits
        flag_bits += str(red_channel_LSB & 1)

    # This is the binary string, so you need to convert the a string that we can understand
    # flag_bits[i:i+8] you need to get every 8 binary values togeter, so you need to slice it into 8 binary each
    # int(flag_bits[i:i+8], 2) This will convert the binary to an integer
    # chr(int(flag_bits[i:i+8], 2)) This will convert the integer to ASCII Code Character
    # for i in range(0, bits_to_extract, 8) This means that we start at 0, we stop when we reach the number of bits we want to exract and we incremenet the loop by 8
    # You want to get every 8 binary values to decode them
    flag_chars = [chr(int(flag_bits[i:i+8], 2)) for i in range(0, bits_to_extract, 8)]

    # You'll concatenate these character.
    flag = ''.join(flag_chars)

    # This is your exracted flag
    print(f"Extracted flag: {flag}")

# In the command line, just run python extract_flag_cool_cat.py with the paramaters (image, seed, flag length)
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_flag_cool_cat.py <image_with_flag> <seed> <flag_length>")
        sys.exit(1)

    image_path = sys.argv[1] # Path to the image
    seed = sys.argv[2] # The seed used for the pseduo-random number generator
    flag_length = int(sys.argv[3]) # The flag length

    extract_flag_cool_cat(image_path, seed, flag_length)


# Command line "python extract_flag_cool_cat.py cool_cat.png 6432 24"
