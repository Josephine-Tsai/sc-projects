"""
File: mirror_lake.py
Name: Josephine
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    This function will build a new picture which looks like scene with mirror lake.
    :param filename: str, 'images/mt-rainier.jpg'
    :return new_img: image, a new image which contains the 'filename' image and the mirror lake
    """
    img = SimpleImage(filename)
    # Create a new blank image which is two times higher than the old image.
    new_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            # Pick up 1 pixel in img, and then put it into 2 places in the new_image.
            pixel = img.get_pixel(x, y)
            p1 = new_img.get_pixel(x, y)
            p2 = new_img.get_pixel(x, new_img.height-1-y)
            p1.red = pixel.red
            p1.green = pixel.green
            p1.blue = pixel.blue
            p2.red = pixel.red
            p2.green = pixel.green
            p2.blue = pixel.blue
    return new_img


def main():
    """
    The user needs to give a picture, and then the program will firstly show the picture.
    After that, putting that picture into the reflect() function to get a new picture(with mirror lake).
    Finally, show the new picture.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
