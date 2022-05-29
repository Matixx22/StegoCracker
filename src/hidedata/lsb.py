from datetime import datetime

import numpy as np
from PIL import Image


def bytes2intarray(data):
    data = bytearray(data)
    bits = []
    for byte in data:
        for shift in range(8 - 1, -1, -1):
            bits.append((byte >> shift) & 1)
    return bits


def hide_in_lsb(filename, to_hide):
    pil_im = Image.open(filename, 'r')
    image = list(pil_im.getdata())
    to_hide = bytes2intarray(to_hide)

    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_image_location = "../../resources/temp/" + str(time) + ".jpg"

    new_image = []
    # Create list with same size as original image
    new_pixel = list(image[0])

    current_pixel = 0
    # iterate over all bits from to_hide message
    for bit in to_hide:
        try:
            color_list = list(image[current_pixel])
            for index in range(0, len(color_list)):
                # change last bit to bit value
                new_pixel[index] = color_list[index] & 254 + bit
        except IndexError:
            raise Exception("Image is to small to hide data")
        new_image.append(tuple(new_pixel))
        current_pixel += 1

    # add rest of the pixels
    if len(new_image) != len(image):
        new_image += image[len(new_image):]

    new_image_array = np.array(new_image).astype('uint8')
    new_image_array = np.reshape(new_image_array[..., np.newaxis], (pil_im.height, pil_im.width, 3))
    Image.fromarray(new_image_array.astype('uint'), mode='RGB').save(new_image_location, 'JPEG')


if __name__ == '__main__':
    file = "../../resources/sample.jpg"
    data = open("../../resources/sample_small.jpg", 'rb').read()

    bytes2intarray(data)
    hide_in_lsb(file, data)
