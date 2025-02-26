### chap08/pair32.py
from PIL import Image
import random

# Your favorite color from https://g.co/kgs/1Ykek2r
# The values of RGB should be between [0,255]
R, G, B = 108, 180, 66

# Adjustment value
adjustment = 80

# Create a new RGB image, initialized to black
sz = (200, 200)
im = Image.new('RGB', sz)
pixels = im.load()

# No cheating
random_condition = random.choice([0, 1])
def get_color(i):
    if i ^ random_condition:
        return (R, G, B)
    else:
        return (R + adjustment, G + adjustment, B + adjustment)

# Set the color of each pixel to the r, g, b values specified above
for i in range(sz[0]):
    for j in range(sz[1]):
        if i < sz[0] / 2 - 10:
            pixels[i,j] = get_color(0)
        elif i > sz[0] / 2 + 10:
            pixels[i,j] = get_color(1)
        else:
            pixels[i,j] = (255, 255, 255)

im.save('images/out.png')
