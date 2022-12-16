import os
from os import listdir
import time


def main():
    # get the path/directory
    #main_dir = "D:\Astral\Document\Programming\Python\ImageToAscii"
    #folder_dir = "D:\Astral\Document\Programming\Python\ImageToAscii\images"
    main_dir = r"C:\Users\jenso\Documents\Programming\Python\VidToASCII"
    image_dir = f"{main_dir}\images"
    os.system(f'cd {main_dir}')

    #prints out all image
    all_images = sorted(os.listdir(image_dir), key=lambda x: int(x.split(".")[0])) 
    for image in all_images:
        #os.system('cmd /c cls')
        print('\033[4A\033[2K', end='')
        #print('\b'*1000)
        print(image)
        os.system(
            f'python {main_dir}\image_to_ascii.py --imagepath {image_dir}\{image}')


if __name__ == "__main__":
    main()

