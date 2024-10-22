import sys
import random
from PIL import Image
import hashlib

def extract_randomized_data_from_red_lsb(image_path, seed, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Set random seed
    int_seed = int.from_bytes(hashlib.sha256(seed.encode()).digest(), 'big')
    random_gen = random.Random(int_seed)
    number_of_pixels = width * height

    # Use random gen to get data positions
    positions = list(range(number_of_pixels))
    random_gen.shuffle(positions)

    # Extract data bits in this order from RED LSB.
    extracted_data_bits = ''
    for pos in positions:
        x = pos % width
        y = pos // width
        red_channel_LSB = pixels[x, y][0]
        extracted_data_bits += str(red_channel_LSB & 1)
    data_bytes = bytes(int(extracted_data_bits[i:i + 8], 2) for i in range(0, len(extracted_data_bits), 8))

    # Dump it into a file
    with open(output_path, 'wb') as output_file:
        output_file.write(data_bytes)

    print(f"Binary data extracted and saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_randomized_data_from_red_lsb.py <image_path> <seed> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    seed = sys.argv[2]
    output_path = sys.argv[3]

    extract_randomized_data_from_red_lsb(image_path, seed, output_path)
