from PIL import Image
import numpy as np
from datetime import datetime


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
    np_image = np.asarray(pil_im)
    # print(np_image)
    to_hide = bytes2intarray(to_hide)

    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_image_location = "../../resources/temp/" + str(time) + ".png"

    new_image = []
    # Create list with same size as original image
    new_pixel = list(image[0])

    current_pixel = 0
    # iterate over all bits from to_hide message
    color = 0
    for bit in to_hide:
        try:
            color_list = list(image[current_pixel])
            # change last bit to bit value
            new_pixel[color] = color_list[color] & 254 + bit
        except IndexError:
            raise Exception("Image is to small to hide data")
        color += 1
        if color == len(new_pixel):
            new_image.append(tuple(new_pixel))
            color = 0
            current_pixel += 1

    # add rest of the pixels
    if len(new_image) != len(image):
        new_image += image[len(new_image):]

    new_image_array = np.array(new_image).astype('uint8')
    new_image_array = np.reshape(new_image_array[..., np.newaxis], (pil_im.height, pil_im.width, 3))
    new_pil_im = Image.fromarray(new_image_array)
    new_pil_im.resize(pil_im.size)
    # new_pil_im.show()
    new_pil_im.save(new_image_location, format='PNG', subsampling=0, quality=100, optimize=False, progressive=True)


if __name__ == '__main__':
    file = "D:\Studia\BOT\PROJEKT/kocham_boty.jpg"
    data = open("D:\Studia\BOT\PROJEKT/nienawidze_botow.jpg", 'rb').read()
    # data = (bytes("1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d0560e0f5302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75", 'utf-8'))
    # data = b'kocham boty'
    bytes2intarray(data)
    hide_in_lsb(file, data)
