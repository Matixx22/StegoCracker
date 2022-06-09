from PIL import Image


def get_data(filename) -> bytes:
    """
    Get from image least significant bits

    Args:
        filename (str): image path

    Raises:
        TODO jak coś będzie

    Returns:
        data (bytes): Data extracted from image

    """
    data = bytes()

    pil_im = Image.open(filename, 'r')
    image = list(pil_im.getdata())
    counter = 0
    bit = [0] * 8
    byte = 0

    for pixel in image:
        for color in range(0,3):
            bit[counter] = pixel[color] & 1

            counter += 1
            # convert 8bits to one byte and add to data
            if counter == 8:
                for i in range(0, 8):
                    byte += (bit[i] << (7 - i))
                data += byte.to_bytes(1, byteorder='big')
                byte = 0
                counter = 0

    # convert left bits to byte if there is any
    if counter > 0:
        for i in range(0, counter):
            byte += (bit[i] << (7 - i))
        data += byte.to_bytes(1, byteorder='big')

    return data


if __name__ == '__main__':
    filename = "../../../resources/temp/2022_05_31_17_18_10.jpg"

    print(get_data(filename).hex())
