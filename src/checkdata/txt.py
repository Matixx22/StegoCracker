import binascii
from textwrap import wrap

# Space, newline, comma, dot, A-Z, a-z, 0-9, dash, underscore, exclamation mark,
# colon, semicolon, question mark, percent
text_ascii_chars = [b'\x20', b'\x0a', b'\x20', b'\x41', b'\x42', b'\x43', b'\x44', b'\x45', b'\x46', b'\x47', b'\x48',
                    b'\x49', b'\x4a', b'\x4b', b'\x4c', b'\x4d', b'\x4e', b'\x4f', b'\x50', b'\x51', b'\x52', b'\x53',
                    b'\x54', b'\x55', b'\x56', b'\x57', b'\x58', b'\x59', b'\x5a', b'\x61', b'\x62', b'\x63', b'\x64',
                    b'\x65', b'\x66', b'\x67', b'\x68', b'\x69', b'\x6a', b'\x6b', b'\x6c', b'\x6d', b'\x6e', b'\x6f',
                    b'\x70', b'\x71', b'\x72', b'\x73', b'\x74', b'\x75', b'\x76', b'\x77', b'\x78', b'\x79', b'\x7a',
                    b'\x2c', b'\x2e', b'\x30', b'\x31', b'\x32', b'\x33', b'\x34', b'\x35', b'\x36', b'\x37', b'\x38',
                    b'\x39', b'\x3a', b'\x3b', b'\x3f', b'\x21', b'\x22', b'\x25', b'\x27', b'\x5f', b'\x2d'
                    ]


def check_data(source) -> {bool, str}:
    """
    Check if there is text in bytes

    Args:
        source (bytes): bytes to check
        output: Folder to save found message

    Raises:
        TODO jak coś będzie

    Returns:
        is_txt (bool): True - bytes contain text, False - bytes don't contain text
        txt (str): Found text

    """
    is_txt = False
    txt = ""

    limit_valid_text = 5
    valid_counter = 0
    source = bytearray(source)
    for byte in source:
        byte = byte.to_bytes(1, byteorder="big")
        if byte in text_ascii_chars:
            txt += byte.decode("utf-8")
            valid_counter += 1
            if valid_counter == limit_valid_text:
                is_txt = True

    return is_txt, txt


# remove later
if __name__ == '__main__':
    text = bytearray.fromhex("4E 69 65 6E 61 77 69 64 7A 65 20 62 6F 74 6F 77 7e")
    data = open("../../resources/sample.jpg", "rb").read()

    check = check_data(data)[1]
    print(check)
