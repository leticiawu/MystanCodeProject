"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: The original image "smiley-face.png".
    :return: The resulting image after applying the blur effect.
    """
    # Get the width and height of the original image
    new_w = img.width
    new_h = img.height

    # Create a new blank image to store the original image
    new_img = SimpleImage.blank(new_w, new_h)

    # 使用迴圈對新圖像的每一個像素像素的 x 和 y 座標進行處理的過程
    for x in range(new_w):
        for y in range(new_h):
            # 初始化new image上的 rgb 值為 0
            total_r = 0
            total_g = 0
            total_b = 0
            count = 0

            # Iterate 3x3 矩陣：為計算當前像素周圍的鄰居像素的平均顏色
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x, neighbor_y = x + i, y + j

                    # 判斷鄰居是否在original image的範圍內
                    if 0 <= neighbor_x < img.width and 0 <= neighbor_y < img.height:
                        # 有：拿鄰居位置的像素
                        pixel = img.get_pixel(neighbor_x, neighbor_y)
                        # 加總所有鄰居顏色的值
                        total_r += pixel.red
                        total_g += pixel.green
                        total_b += pixel.blue
                        count += 1
            # 得平均顏色的值
            avg_r = total_r / count
            avg_g = total_g / count
            avg_b = total_b / count

            # 問：更新到new image上 是錯在這裡嗎？
            new_img.set_pixel(x, y, SimpleImage(avg_r, avg_g, avg_b))
            # new_img.set_pixel(x, y, SimpleImage.set_rgb(red=avg_r, green=avg_g, blue=avg_b))

    return new_img


def main():
    """
    Process the blur effect to 'smiley-face.png' and display the result.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# 設（x, y）為當前像素的座標，要迭代的周圍鄰居為:

# (x-1, y-1)   (x, y-1)   (x+1, y-1)
# (x-1, y)     (x, y)     (x+1, y)
# (x-1, y+1)   (x, y+1)   (x+1, y+1)
# 範圍從 -1 到 1 的整數，要寫到 2 上限不包含


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
