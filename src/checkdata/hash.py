def check_data(source) -> {bool}:
    """
    Check if there is hash in bytes

    Args:
        source (str): string to check

    Raises:
        TODO jak coś będzie

    Returns:
        is_hash (bool): True - str contain hash, False - str don't contain hash

    """
    # TODO better hash searching
    is_hash = False
    hash = ""

    hash_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]

    hash_length = [128, 160, 192, 256, 384, 512]

    matched_list = [characters in hash_chars for characters in source]

    if all(matched_list) and len(source) in [length/4 for length in hash_length]:
        is_hash = True

    return is_hash, hash


if __name__ == '__main__':
    if check_data("5a5dc3936c05c32e61aa539e7ffb40ca"):
        print("to może być hash")
