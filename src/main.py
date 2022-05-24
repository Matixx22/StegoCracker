from getdata import icmp_get_data
from getdata import image_get_lsb
from getdata import html_get_tags

from checkdata import check_hash
from checkdata import check_jpg
from checkdata import check_pdf
from checkdata import check_txt

import argparse
import os
from datetime import datetime


def _write_binary(data: bytes, path: str):
    file = open(path, 'wb')
    file.write(data)


def get_filetype(file):
    data = bytearray(open(file, 'rb').read(20))

    pcap_signature = [b'\x0A\x0D\x0D\x0A', b'\xA1\xB2\xC3\xD4', b'\x4D\x3C\xB2\xA1', b'\xA1\xB2\x3C\x4D']
    jpg_signature = [b'\xff\xd8\xff']
    html_signature = [b'<html', b'<Html', b'<hTml', b'<htMl', b'<htmL',
                      b'<HTml', b'<HtMl', b'<HtmL', b'<hTMl', b'<hTmL',
                      b'<htML', b'<HTMl', b'<HTmL', b'<HtML', b'<hTML',
                      b'<HTML', ]

    # pcap
    for signature in pcap_signature:
        if data[:len(signature)] == signature:
            return 'pcap'

    # jpg
    for signature in jpg_signature:
        if data[:len(signature)] == signature:
            return 'jpg'

    # html
    for signature in html_signature:
        if data[:len(signature)] == signature:
            return 'html'


def getdata(infile: str):
    infile_type = get_filetype(infile)

    if infile_type == 'html':
        return html_get_tags(infile)

    elif infile_type == 'jpg':
        return image_get_lsb(infile)

    elif infile_type == 'pcap':
        return icmp_get_data(infile)


def main():
    # args
    parser = argparse.ArgumentParser(description="StegoCracker - easy way to crack steganography")

    parser.add_argument('file', help='A file to search for hidden message')
    parser.add_argument('-o', '--output', default="temp", help='Full path for folder for found messages')

    args = parser.parse_args()

    infile = args.file
    data = getdata(infile)
    output = args.output
    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    if not os.path.isdir(output):
        print(f'\033[31;1m[+] Creating directory {output}\033[0m')
        os.mkdir(output)

    jpg = check_jpg(data, output)
    if jpg[0]:
        print(f'\033[33;1m[+] Found jpg in {infile} and saved it in {jpg[1]}\033[0m')

    pdf = check_pdf(data, output)
    if pdf[0]:
        print(f'\033[33;1m[+] Found pdf in {infile} and saved it in {pdf[1]}\033[0m')

    exe_output = output
    # # exe
    # if check_jpg(data)[0]:
    #     print(f'\033[31;1m[-] Found jpg in {infile} and saved it in {output}\033[0m')

    txt_output = output + "/" + time + ".txt"
    txt = check_txt(data)
    if txt[0]:
        open(txt_output, 'w').write(txt[1])
        print(f'\033[33;1m[+] Found txt in {infile} and saved it in {txt_output}\033[0m')
        hash_output = output + "/" + time + ".hash"
        hash = check_hash(txt[1])
        if hash[0]:
            open(hash_output, 'w').write(hash[1])
            print(f'\033[33;1m[+] Found hash in {infile} and saved it in {output}\033[0m')


if __name__ == '__main__':
    main()
