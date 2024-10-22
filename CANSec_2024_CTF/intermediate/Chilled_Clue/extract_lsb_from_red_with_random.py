# This has only small difference but doesn't work because shuffle uses 2D array (x,y)
# has less number of items than the other one where all items spread into a 1D array.
import sys
import random
from PIL import Image

def extract_lsb_from_red_with_random(image_path, seed, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Set random seed
    random_gen = random.Random(seed)
    number_of_pixels = width * height

    # Difference is here
    # Use random gen to get data positions
    positions = [(x, y) for x in range(width) for y in range(height)]
    random_gen.shuffle(positions)

    # Extract data bits in this order from RED LSB.
    extracted_data_bits = ''
    for x, y in positions:
        red_channel_LSB = pixels[x, y][0]
        extracted_data_bits += str(red_channel_LSB & 1)
    data_bytes = bytes(int(extracted_data_bits[i:i + 8], 2) for i in range(0, len(extracted_data_bits), 8))

    # Dump it into a file
    with open(output_path, 'wb') as output_file:
        output_file.write(data_bytes)

    print(f"Binary data extracted and saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_lsb_from_red_with_random.py <image_path> <seed> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    seed = sys.argv[2]
    output_path = sys.argv[3]

    extract_lsb_from_red_with_random(image_path, seed, output_path)
