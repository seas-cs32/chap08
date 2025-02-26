### chap08/create_gif.py
'''
Code from Google's Generative AI system running in search. The
prompt was "python library to create a gif".
'''
import sys
from PIL import Image

def create_gif(filenames, gifname, duration=100):
    """Creates a GIF from a list of image filenames.

    Args:
        filenames: A list of paths to image files.
        gifname: Filename where the function save the created GIF.
        duration: The duration of each frame in milliseconds (default: 100).
    """
    images = [Image.open(filename) for filename in filenames]
    images[0].save(
        gifname,
        format='GIF',
        append_images=images[1:],
        save_all=True,
        duration=duration,        # duration of each frame in milliseconds
        loop=0                    # 0 means loop indefinitely
    )

def main():
    # Check for proper usage
    if len(sys.argv) == 4:
        # Grab the root image filename and extension
        root, extension = sys.argv[1].split('.')

        # Grab the number of image files
        num_files = int(sys.argv[2])

        # Build the list of image files
        filenames = []
        for i in range(num_files):
            filenames.append(f'images/{root}{i + 1}.{extension}')

        # Grab the output GIF filename
        gifname = sys.argv[3]

    else:
        sys.exit("Usage: python3 create_gif.py root_fname num_files gif_fname")

    print('Read files:', filenames)
    create_gif(filenames, gifname, 200)
    print('Wrote GIF to:', gifname)

if __name__ == '__main__':
    main()
