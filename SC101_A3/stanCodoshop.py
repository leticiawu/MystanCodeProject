"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    color_dist = ((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2) ** 0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_r = 0
    total_g = 0
    total_b = 0

    for pixel in pixels:
        total_r += pixel.red
        total_g += pixel.green
        total_b += pixel.blue

    num_pixels = len(pixels)
    red = total_r // num_pixels
    green = total_g // num_pixels
    blue = total_b // num_pixels

    rgb = [red, green, blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # 步驟1: 計算平均顏色值
    avg_point = get_average(pixels)
    # 步驟2: 計算顏色的距離
    # 步驟3: 找到距離最小、最接近的pixel

    # 設定min_dist 和 best_pixel 初始值
    min_dist = []
    best = []

    for pixel in pixels:
        dist = ((pixel.red - avg_point[0]) ** 2 + (pixel.green - avg_point[1]) ** 2 + (pixel.blue - avg_point[2]) ** 2) \
               ** 0.5

        if dist < min_dist:
            min_dist = dist
            best = pixel

    return best

    # 目前得到的best值不對


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #

    for x in range(width):  # 得寬
        for y in range(height):     # 得高
            pixel_position = []     # 空字串存每個x, y位置的像素值

            for image in images:    # 每ㄧ個圖像都跑過ㄧ遍
                pixel_position.append(image.get_pixel(x, y))    # 當前像素添加到pixel_position的list中

                best_pixel = get_best_pixel(pixel_position)     # 找到pixel_position’s list中最接近平均值的pixel

                # 將 best_pixel 的 RGB 對應到的位置給圖像
                result.pixel.red = best_pixel.red
                result.pixel.green = best_pixel.green
                result.pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
