# This program converts a video to frames
# Created By: Astral

# Update to readme
# to use: python app.py --videopath [filepath]
import sys
import argparse


def main():
    # Creates argument parser
    parser = argparse.ArgumentParser(
        description="This program converts an image into ASCII art.")
    # Adding expected arguments
    parser.add_argument('--videopath', dest='vidFile', required=True)
    # parse args
    args = parser.parse_args()
    imgFile = args.vidFile

    # Prints ascii
    for ascii in ascii_str_arr:
        print(ascii)


if __name__ == "__main__":
    main()
