from getdata import icmp_get_data
from getdata import image_get_lsb
from getdata import html_get_tags

from checkdata import check_hash
from checkdata import check_jpg
from checkdata import check_pdf
from checkdata import check_txt

import argparse
import os


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


def main():
    # args
    parser = argparse.ArgumentParser(description="StegoCracker - easy way to crack steganography")

    parser.add_argument('file', help='A file to search for hidden message')
    parser.add_argument('-o', '--output', default="temp", help='Folder for found messages')

    args = parser.parse_args()

    infile = args.file
    output = args.output

    if not os.path.isdir(output):
        print(f'\033[31;1m[-] Creating directory {os.curdir+output}\033[0m')





if __name__ == '__main__':
    # main()
    print(get_filetype("../resources/html/index.html"))
    # html_filename = "./example.html"
    # pcap_filename = "./example.pcap"
    # img_filename = "./example.jpg"
    #
    # find_steg(html_get_lower_letters(html_filename))
    # find_steg(html_get_upper_letters(html_filename))
    # find_steg(icmp_get_data(pcap_filename))
    # find_steg(image_get_lsb(img_filename))
