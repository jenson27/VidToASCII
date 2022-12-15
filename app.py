import os
from os import listdir
import time


def main():
    # get the path/directory
    main_dir = "D:\Astral\Document\Programming\Python\ImageToAscii"
    folder_dir = "D:\Astral\Document\Programming\Python\ImageToAscii\images"
    os.system(f'cd {main_dir}')
    for images in os.listdir(folder_dir):
        os.system('cls')

        # check if the image ends with png
        if (images.endswith(".jpg")):
            os.system("cd")
            os.system(
                f'python {main_dir}\image_to_ascii.py --imagepath {folder_dir}\{images}')


if __name__ == "__main__":
    main()
