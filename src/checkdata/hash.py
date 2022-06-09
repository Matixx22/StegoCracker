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

    for index in range(0, len(source)):
        char = source[index]
        if char in hash_chars:
            for length in sorted(hash_length, reverse=True):
                try:
                    end = index+int(length/4)
                    matched_list = [characters in hash_chars for characters in source[index:end]]
                    if all(matched_list) and len(matched_list) == length/4:
                        is_hash = True
                        hash = source[index:end]
                        return is_hash, hash
                except:
                    pass

    return is_hash, hash


if __name__ == '__main__':
    check = check_data("1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d0560e0f5302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75")
    filename = "../../resources/temp/2022_05_28_21_41_03.jpg"
    data = open(filename, 'rb').read()
    check = check_data(data)
    print(check[0])
    print(check[1])

