import math
import itertools
from PIL import Image
import random

# IMAGE_SIZE = (11100, 1200)
IMAGE_SIZE = (1000, 1000)
PIXEL_SPACING = 3

def spaced_range(max, spacing):
    return list(range(max))[0::spacing + 1]
    
def find_pixels(image_path, pixel_spacing):
    source = Image.open(image_path)
    x_values = list(range(source.size[0]))[0::pixel_spacing + 1]
    y_values = 
    for x in :
        for y in list(range(source.size[1]))[0::pixel_spacing + 1]:
            alpha = source.getpixel((x, y))[3]
            if alpha == 255:
                source.putpixel((x, y), (255, 0, 0))
            elif alpha < 255 and alpha > 0:
                source.putpixel((x, y), (0, 255, 0))
            else:
                source.putpixel((x, y), (0, 0, 255))

    source.show()

def generate_them(image_size, pixel_spacing):
    im = Image.new(mode = "RGB", size=IMAGE_SIZE, color=(0, 0, 255))

    blank_pixels = list(itertools.product(spaced_range(image_size[0], pixel_spacing), spaced_range(image_size[1], pixel_spacing)))

    count = 0
    total = len(blank_pixels)

    while blank_pixels:
        rand_pixel = random.choice(blank_pixels)
        blank_pixels.remove(rand_pixel)
        im.putpixel(rand_pixel, (255, 0, 0))
        count += 1
        if count%1000 == 0:
            print(count, total, sep="/")

    im.show()

if __name__ == "__main__":
    # generate_them(IMAGE_SIZE, PIXEL_SPACING)
    find_pixels("./left.png", PIXEL_SPACING)