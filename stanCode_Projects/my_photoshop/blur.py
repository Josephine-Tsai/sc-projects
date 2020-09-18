"""
File: blur.py
Name: Josephine
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    This function can blur the picture.
    :param old_img: image, the original image "images/smiley-face.png"
    :return new_img: image, the blurred 'old_img'
    """
    # Create a new blank image which is as big as the original image.
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            # Pick up a pixel which we want to record new value.
            new_pixel = new_img.get_pixel(x, y)
            count = 0
            pixel_red = 0
            pixel_green = 0
            pixel_blue = 0
            # Get the total value of 9 (the central one + other nearest 8) pixels (the red/green/blue value).
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Make sure all the pixels are in the scale of image.
                    if old_img.width > (x+i) >= 0 and old_img.height > (y+j) >= 0:
                        avg_pixel = old_img.get_pixel(x+i, y+j)
                        pixel_red += avg_pixel.red
                        pixel_green += avg_pixel.green
                        pixel_blue += avg_pixel.blue
                        count += 1
            # Calculate the average value of 9 pixels and record it into the pixel we picked(new_pixel).
            new_pixel.red = pixel_red//count
            new_pixel.green = pixel_green//count
            new_pixel.blue = pixel_blue//count
    return new_img


def main():
    """
    The user needs to give a picture, and the program will firstly show the picture.
    Then the program will use the blur() function to blur the picture for one time.
    And then put it into a for loop to run the blur() function for several times.
    Finally, show that picture.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
