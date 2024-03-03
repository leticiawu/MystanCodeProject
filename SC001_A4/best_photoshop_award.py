"""
File: best_photoshop_award.py
Name: Leticia
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.5
MIN_BRIGHTNESS = 50


def main():
    """
    The crane standing on the moon surface.
    """
    foreground = SimpleImage('image_contest/crane_1920x1769.jpg')
    background = SimpleImage('image_contest/nasa_2400x2400.jpg')
    background.make_as_big_as(foreground)
    new_img = combine(foreground, background)
    new_img.show()


def combine(foreground, background):
    # Loop over all pixels in the foreground image.
    for x in range(foreground.width):
        for y in range(foreground.height):
            # Get the current pixel in the foreground image.
            pixel = foreground.get_pixel(x, y)
            # Calculate the average and total of the RGB values.
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            total = pixel.red + pixel.green + pixel.blue
            # Check if the pixel is green enough and not too dark.
            if pixel.green > avg * THRESHOLD and total > MIN_BRIGHTNESS:
                # Replace green pixel with the corresponding background pixel.
                bg_pixel = background.get_pixel(x, y)
                pixel.red = bg_pixel.red
                pixel.green = bg_pixel.green
                pixel.blue = bg_pixel.blue
    return foreground


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
