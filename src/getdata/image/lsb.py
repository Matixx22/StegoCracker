import os
import io
import numpy as np
import PIL.Image as Image

def to_bin(data):
    """
    Converts the data to binary
    
    """
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.unit8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported")

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
    # Code goes here...
    
    if not os.path.exists(filename):
        print("\033[92m[!] Image not found\033[00m")
        return
    print("\033[92mDecodingMode : On\033[0m \n\033[92m[*] Please wait...\033[0m \n\033[92m[*] Decoding...\033[0m")
    
    # read the image

    # Convert image to bytes
   
    pil_im = Image.fromarray(filename)
    b = io.BytesIO()
    pil_im.save(b, 'jpeg')
    image = b.getvalue()
    data = b''
    
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            data += r[-1]
            data += g[-1]
            data += b[-1]
    # split by 8-bits
    all_bytes = [data[i: i + 8] for i in range(0, len(data), 8)]


    return all_bytes




