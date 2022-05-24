from datetime import datetime

def _write_binary(data: bytes, path: str):
    file = open(path, 'wb')
    file.write(data)

def check_data(source, output: str = "../../resources/temp/") -> {bool, str}:
    """
    Check if there is pdf in bytes

    Args:
        source (bytes): bytes to check
        output: Folder to save found message

    Raises:
        TODO jak coś będzie

    Returns:
        is_pdf (bool): True - bytes contain pdf, False - bytes don't contain pdf
        pdf_location (str): Location of the new pdf file

    """
    is_pdf = False
    pdf_location = ""

    pdf_signature = b'\x25\x50\x44\x46'
    pdf_end_signature = b'\x25\x25\x45\x4F\x46'

    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # Code goes here...

    # Simple check
    if pdf_signature in source and pdf_end_signature in source:
        is_pdf = True
        pdf_start_index = source.index(pdf_signature)
        pdf_end_index = source.index(pdf_end_signature) + len(pdf_end_signature)
        pdf_bytes = source[pdf_start_index:pdf_end_index]
        # write bytes to new file
        pdf_location = "../../resources/temp/" + str(time) + ".pdf"
        _write_binary(pdf_bytes, pdf_location)

    return is_pdf, pdf_location


# remove later
if __name__ == '__main__':
    filename = "../../resources/simple.pdf"
    data = open(filename, 'rb').read()
    if check_data(data)[0]:
        print("Wszystko działa mordo!")
