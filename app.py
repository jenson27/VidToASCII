import os
from os import listdir
import time
from image_to_ascii import main2 as image_ascii


def animate(filepath):
    """
    Takes in a filepath as argument and loop through the txt files and print
    """

    # sort out all text files
    all_text = sorted(os.listdir(filepath),
                      key=lambda x: int(x.split(".")[0]))

    for text in all_text:
        print('\033[4A\033[2K', end='')
        log = open(f"{filepath}/{text}", "r").read()
        print(log)
        time.sleep(0.01)


def generate_ascii_file(all_images, main_dir, image_dir, text_dir):
    """
    Convert image to ascii text file
    """
    counter = 0
    for image in all_images:
        # os.system(
        #    f'python {main_dir}\image_to_ascii.py --imagepath {image_dir}\{image} --textpath {text_dir}\{counter}.txt')
        image_ascii(f"{image_dir}\{image}", f"{text_dir}\{counter}.txt")
        counter += 1


def main():
    # get the path/directory
    main_dir = "D:\Astral\Document\Programming\Python\ImageToAscii"
    folder_dir = "D:\Astral\Document\Programming\Python\ImageToAscii\images"
    #main_dir = r"C:\Users\jenso\Documents\Programming\Python\VidToASCII"
    image_dir = f"{main_dir}\images"
    text_dir = f"{main_dir}\\text"
    os.system(f'cd {main_dir}')

    # sort out all image
    all_images = sorted(os.listdir(image_dir),
                        key=lambda x: int(x.split(".")[0]))

    # Clear image directory
    #os.system(f"del /S {text_dir}\*")
    #generate_ascii_file(all_images, main_dir, image_dir, text_dir)

    animate(text_dir)


if __name__ == "__main__":
    main()
