import re


def hide(filename, to_hide: bytearray):
    file = open(filename, 'r', encoding="utf8")
    data = file.read()
    tags = re.findall(r'<[^>]+>', data)
    new_tags = []
    # for index in range(length-1, -1, -1):
    #     for bit in range(0, 8):
    #         print((to_hide[index] >> bit) & 1)
    # print(int.from_bytes(to_hide[], byteorder='big'))
    current_bit = 7
    current_byte = 0
    for tag in tags:
        # get text from tag
        t = re.sub(r'(<\w+)[^>]*(>)', r'\1\2', tag)
        t = re.sub('[/<>1-9]', '', t)
        new_t = ""
        # change to upper when 1, otherwise lower
        for char in t:
            if current_byte < len(to_hide):
                value = to_hide[current_byte] >> current_bit & 1
                if value == 1:
                    char = char.upper()
                else:
                    char = char.lower()

                if current_bit == 0:
                    current_byte += 1
                    current_bit = 8
                current_bit -= 1
            else:
                char = char.lower()
            new_t += char
        # change to new t in tag
        new_tags.append(tag.replace(t, new_t))
    index = 0
    previous_index = 0
    while True:
        find = data[previous_index:index].find(tags[0])
        if find >= 0:
            previous_index += find
            data = data[:previous_index] + new_tags[0] + data[index:]
            tags.pop(0)
            new_tags.pop(0)
        index += 1
        if len(tags) == 0:
            break
    return data


if __name__ == '__main__':
    file = "D:/kgrzegorzewski/Downloads/pw.html"
    to_hide_file = open("../../resources/sample_small.jpg", 'rb')
    to_hide = bytearray(to_hide_file.read())
    print(hide(file, to_hide))
