import itertools
import PIL
import PIL.Image
import random

IMAGE_SIZE = (11100, 1200)

PIXEL_SPACING = 4

im = PIL.Image.new(mode = "RGB", size=IMAGE_SIZE, color=(0, 0, 255))

blank_pixels = list(itertools.product(list(range(IMAGE_SIZE[0]))[0::PIXEL_SPACING], list(range(IMAGE_SIZE[1]))[0::PIXEL_SPACING]))

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