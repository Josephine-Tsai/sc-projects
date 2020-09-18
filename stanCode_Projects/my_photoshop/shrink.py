"""
File: shrink.py
Name: Josephine
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    This function can shrink the picture (make the width and height become 1/2).
    :param filename: str, "images/poppy.png"
    :return new_img: SimpleImage, the shrank 'ori_img'
    """
    ori_img = SimpleImage(filename)
    # Create a new blank image which is 1/4 big as the original image.
    new_img = SimpleImage.blank(ori_img.width//2, ori_img.height//2)
    for x in range(0, ori_img.width, 2):
        for y in range(0, ori_img.height, 2):
            # Pick up a pixel which we want to record new value.
            new_pixel = new_img.get_pixel(x/2, y/2)
            count = 0
            pixel_red = 0
            pixel_green = 0
            pixel_blue = 0
            # Get the total value of 4 pixels (the red/green/blue value).
            # Record 4 pixels into 1 pixel, so the picture can be shrank.
            for i in range(2):
                for j in range(2):
                    # Make sure all the pixels are in the scale of image.
                    if ori_img.width > (x+i) >= 0 and ori_img.height > (y+j) >= 0:
                        avg_pixel = ori_img.get_pixel(x+i, y+j)
                        pixel_red += avg_pixel.red
                        pixel_green += avg_pixel.green
                        pixel_blue += avg_pixel.blue
                        count += 1
            # Calculate the average value of 4 pixels and record it.
            new_pixel.red = pixel_red//count
            new_pixel.green = pixel_green//count
            new_pixel.blue = pixel_blue//count
    return new_img


def main():
    """
    The user needs to give a picture, and the program will firstly show the picture.
    Then the program will use the shrink() function to shrink the picture.
    Finally, show the shrank picture.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
