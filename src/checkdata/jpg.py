from datetime import datetime


def _write_binary(data: bytes, path: str):
    file = open(path, 'wb')
    file.write(data)


def check_data(source: bytes, output: str = ".") -> {bool, str}:
    """
    Check if there is jpg in bytes

    Args:
        source (bytes): bytes to check
        output: Folder to save found message

    Raises:
        TODO jak coś będzie

    Returns:
        is_jpg (bool): True - bytes contain jpg, False - bytes don't contain jpg
        jpg_location (str): Location of the new jpg file

    """
    is_jpg = False
    jpg_location = ""

    jpg_signature = b'\xff\xd8\xff'
    jpg_end_signature = b'\xff\xd9'

    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # Code goes here...

    # Simple check
    if jpg_signature in source and jpg_end_signature in source:
        is_jpg = True
        jpg_start_index = source.index(jpg_signature)
        jpg_end_index = source.index(jpg_end_signature) + len(jpg_end_signature)
        jpg_bytes = source[jpg_start_index:jpg_end_index]
        # write bytes to new file
        jpg_location = output + "/" + str(time) + ".jpg"
        _write_binary(jpg_bytes, jpg_location)

    return is_jpg, jpg_location


# delete later
if __name__ == '__main__':
    filename = "../../tests/res/lsb/jpg_in_jpg.jpg"
    # only bytes from file
    jpg_file = open(filename, "rb")
    data = b'\xaa\xaa\xbb'
    data += jpg_file.read()
    full_jpg = data
    jpg_file.close()

    # only every second byte is from file
    # I think we should make it every two bit (not byte)
    # Just do another function in main file which will extract every two bits
    # and then use check_data() functions
    data = bytes()
    jpg_file = open(filename, "rb")

    byte = jpg_file.read(1)
    while byte != b"":
        data += byte
        data += b'\xaa'
        byte = jpg_file.read(1)
    hide_jpg = data

    check_data(full_jpg)
