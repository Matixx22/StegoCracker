from datetime import datetime


def _write_binary(data: bytes, path: str):
    file = open(path, 'wb')
    file.write(data)


def check_data(source, output: str = "../../resources/temp/") -> {bool, str}:
    """
    Check if there is exe in bytes

    Args:
        source (bytes): bytes to check
        output: Output folder to save found message (default: ../../resources/temp/"

    Raises:


    Returns:
        is_exe (bool): True - bytes contain exe, False - bytes don't contain exe
        exe_location (str): Location of the new exe file
    """
    is_exe = False
    exe_location = ""

    exe_signature = b'\x4D\x5A'

    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    source = bytearray(source)
    if exe_signature in source:
        is_exe = True
        start_index = source.index(exe_signature)
        exe_bytes = source[start_index:]
        exe_location = output + str(time) + ".exe"
        _write_binary(exe_bytes, exe_location)

    return is_exe, exe_location


# delete later
if __name__ == '__main__':
    filename = "../../resources/sample.exe"
    data = open(filename, 'rb').read()

    print(check_data(data))
