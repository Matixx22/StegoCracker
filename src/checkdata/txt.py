import binascii
from textwrap import wrap


def check_data(source) -> {bool, str}:
    """
    Check if there is text in bytes

    Args:
        source (bytes): bytes to check

    Raises:
        TODO jak coś będzie

    Returns:
        is_txt (bool): True - bytes contain text, False - bytes don't contain text
        txt (str): Found text

    """
    is_txt = False
    txt = ""

    # Code goes here...

    txt += text_from_bits(source)

    # TODO: Change this to more reasonable solution
    is_txt = True

    return is_txt, txt


def text_from_bits(bits, encoding='utf-8'):
    text = ''
    bits_list = wrap(bits.decode(), 8)

    # Print for debugging
    print(bits_list)

    # TODO: Probably error handling on this is needed but no errors occurred during testing invalid bytes -> ascii
    for chunk in bits_list:
        n = int(chunk, 2)
        text += int2bytes(n).decode(encoding)

    return text


def int2bytes(i):
    hex_string = '%x' % i

    if hex_string == 0:
        return
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
