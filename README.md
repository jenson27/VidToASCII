# VidToASCII
Convert a video into ascii text frame by frame and play it

## How does it work?
- Takes a video as input
- Converts the video into individual image frames
- Translates each frame into ASCII characters
- Plays the ASCII animation frame by frame in the command prompt

## image_to_ascii.py
- Converts an image into ASCII art and save it into a text file

```
> image_to_ascii.py --imagepath [filepath] --textpath [filepath]
```
### Options

- --imagepath : File path of image to be converted
- --textpath: Output path for text file


## video_to_image.py
- Converts an video into image frame by frame

```
> image_to_ascii.py --inputpath [filepath] --outputpath [filepath]
```

### Options

- --inputpath : File path of video to be converted
- --outputpath: Output path for images to be stored in


## How to Run?
```
python app.py
```

### Libary
Install the required library to run
- `pip Install Pillow`
- `pip Install Numpy`
