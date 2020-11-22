# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import sys

import cv2
import os


def main(args):
    image = cv2.imread(args.image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # write the grayscale image to disk as a temporary file so we can apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    return parser.parse_args(args)


if __name__ == '__main__':
     sys.exit(main(parse_args(sys.argv[1:])))