# This program converts a image to ascii art
# Created By: Astral

# Update to readme
# to use: python app.py --imagepath [filepath]

import sys
import argparse
import math
from PIL import Image
import numpy as np


def getAverageL(image):
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)

    # get shape
    w, h = im.shape

    # get average
    return np.average(im.reshape(w*h))


def convert_image_to_Ascii(image, cols, scale, moreHeight):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images
    """

    # 70 levels of gray
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # 10 levels of gray
    gscale2 = '@%#*+=-:. '

    # store dimensions
    W, H = image.size[0], image.size[1]
    #print("input image dims: %d x %d" % (W, H))

    # compute width of tile
    w = W/cols

    # compute tile height based on aspect ratio and scale
    h = w/scale

    # compute number of rows
    rows = int(W/w)

    #print("cols: %d, rows: %d" % (cols, rows))
    #print("tile dims: %d x %d" % (w, h))

    # Checks if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
    aimg = ""
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct last tile
        if j == rows-1:
            y2 = H

        # append an empty string
        # aimg.append("")
        aimg += ""

        for i in range(cols):

            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)

            # correct last tile
            if i == cols-1:
                x2 = W

            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getAverageL(img))

            # look up ascii char
            if moreHeight:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

            # append ascii char to string
            #aimg[j] += gsval
            aimg += gsval
        aimg += "\n"

    # return txt image
    return aimg


def write_to_file(filename, lines):
    '''
    Write to a text file given an array of string
    '''
    with open(filename, "w") as txt_file:
        #txt_file.write('\n'.join(line for line in lines))
        txt_file.write(lines)


def main2(imgFile, txtFile):
    # open image and convert to grayscale
    image = Image.open(imgFile).convert('L')
    ascii_str = convert_image_to_Ascii(image, 140, 2, True)

    # Save to text file if imagepath is provided
    if txtFile:
        write_to_file(txtFile, ascii_str)
    else:
        print(ascii_str)


def main():
    # Creates argument parser
    parser = argparse.ArgumentParser(
        description="This program converts an image into ASCII art.")
    # Adding expected arguments
    parser.add_argument('--imagepath', dest='imgFile', required=True)
    # Adding expected arguments
    parser.add_argument('--textpath', dest='txtFile')
    # parse args
    args = parser.parse_args()
    imgFile = args.imgFile

    # open image and convert to grayscale
    image = Image.open(imgFile).convert('L')

    # Note col param is used to determine row
    ascii_str = convert_image_to_Ascii(image, 170, 2, True)

    # Save to text file if imagepath is provided
    if args.txtFile:
        write_to_file(args.txtFile, ascii_str)
    else:
        print(ascii_str)


if __name__ == "__main__":
    main()
