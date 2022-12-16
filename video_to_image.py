# This program converts a video to frames
# Created By: Astral

# Update to readme
# to use: python app.py --videopath [filepath]
import sys
import argparse
import cv2


def extractImages(pathIn, pathOut):
    """
    Convert video into images
    """
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    count = 0
    success = True

    # Extract frame and convert to image
    while success:
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        cv2.imwrite(pathOut + "\\%d.jpg" % count, image)
        count += 1


def main():
    # Creates argument parser
    parser = argparse.ArgumentParser(
        description="This program converts an image into ASCII art.")
    # Adding expected arguments
    parser.add_argument('--inputpath', dest='vidFile', required=True)
    parser.add_argument("--outputpath", dest='outputPath',
                        help="path to images", required=True)
    # parse args
    args = parser.parse_args()
    vidPath = args.vidFile
    outputPath = args.outputPath
    extractImages(vidPath, outputPath)


if __name__ == "__main__":
    main()
