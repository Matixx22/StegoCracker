from datetime import datetime
import os


def _write_binary(data: bytes, path: str):
    file = open(path, 'wb')
    file.write(data)


def check_data(source: bytes, output: str = "../../resources/temp/") -> {bool, str}:
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
    filename = "../../resources/temp/2022_05_28_21_41_03.jpg"
    data = open(filename, 'rb').read()
    check_data(data)
