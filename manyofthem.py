import math
import itertools

from PIL import Image
import random

# constants
IMAGE_SIZE = (11100, 1200)
PIXEL_SPACING = 10

# get list of numbers from 0 to max with spacing between them
def spaced_range(max, spacing):
    return list(range(max))[0::spacing]

def generate_them(image_size, pixel_spacing):
    canvas = Image.new(mode = "RGBA", size=IMAGE_SIZE, color=(0, 0, 0, 0))
    them = [Image.open("./left.png", mode = "r"), Image.open("./right.png", mode = "r")]

    # create a list of all blank pixels in the image, spaced out so that we dont have to check 1.5 million pixels
    blank_pixels = list(itertools.product(spaced_range(image_size[0], pixel_spacing), spaced_range(image_size[1], pixel_spacing)))

    total = len(blank_pixels)

    while blank_pixels:
         # pick a random Them and rotate them
        angle = random.randrange(-30, 30, 1)
        one_of_them = random.choice(them).rotate(angle = angle, expand = True)

        # pick a random blank point and paste Them centered on that point
        x_offset = math.floor(one_of_them.size[0] / 2)
        y_offset = math.floor(one_of_them.size[1] / 2)
        rand_pixel = random.choice(blank_pixels)
        top_left = (rand_pixel[0] - x_offset, rand_pixel[1] - y_offset)
        canvas.paste(one_of_them, top_left, one_of_them)

        # check all of the possible points in that range to see if we can mark them as not blank
        for x in range(top_left[0] + x_offset % pixel_spacing, top_left[0] + x_offset % pixel_spacing + one_of_them.size[0])[0::pixel_spacing]:
            for y in range(top_left[1] + y_offset % pixel_spacing, top_left[1] + y_offset % pixel_spacing + one_of_them.size[1])[0::pixel_spacing]:
                if (x >= 0 and x < canvas.size[0] and y >= 0 and y < canvas.size[1] and canvas.getpixel((x, y))[3] == 255 and (x,y) in blank_pixels):
                    blank_pixels.remove((x, y))
        print(f"{round(100 - 100 * len(blank_pixels) / total, 1)}% ", end="\r")

    canvas.show()

if __name__ == "__main__":
    generate_them(IMAGE_SIZE, PIXEL_SPACING)
