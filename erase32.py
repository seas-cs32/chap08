### chap08/erase32.py -- similar to ALE 8.2, steps 1-4
import sys
import statistics
from PIL import Image

# Check for proper usage and grab the root image filename
if len(sys.argv) == 2:
    root, extension = sys.argv[1].split('.')
    imfile1 = f'images/{root}1.{extension}'
else:
    sys.exit("Usage: python3 erase32.py root_of_image_fname")

with Image.open(imfile1) as im1:
    # Create a new image free of a photobomb
    clean = Image.new(im1.mode, im1.size)

    # INSERT your code here

    clean.save('images/out.png')
