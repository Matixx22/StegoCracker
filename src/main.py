from getdata import icmp_get_data
from getdata import image_get_lsb
from getdata import html_get_tags

from checkdata import check_hash
from checkdata import check_jpg
from checkdata import check_pdf
from checkdata import check_txt
from checkdata import check_exe

import argparse
import os
from datetime import datetime
from threading import Thread
from distutils.spawn import find_executable

from cracker import PasswordCracker


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


def exe(infile, data, output):
    exe = check_exe(data, output)
    if exe[0]:
        print(f'\033[32;1m[-] Found exe in {infile} and saved it in {exe[1]}\033[0m')


def jpg(infile, data, output):
    jpg = check_jpg(data, output)
    if jpg[0]:
        print(f'\033[32;1m[+] Found jpg in {infile} and saved it in {jpg[1]}\033[0m')


def pdf(infile, data, output):
    pdf = check_pdf(data, output)
    if pdf[0]:
        print(f'\033[32;1m[+] Found pdf in {infile} and saved it in {pdf[1]}\033[0m')


def txt_hash(infile, data, output):
    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    txt_output = output + "/" + time + ".txt"
    txt = check_txt(data)
    if txt[0]:
        open(txt_output, 'w').write(txt[1])
        print(f'\033[32;1m[+] Found txt in {infile} and saved it in {txt_output}\033[0m')
        hash_output = output + "/" + time + ".hash"
        hash = check_hash(txt[1])
        if hash[0]:
            open(hash_output, 'w').write(hash[1])
            print(f'\033[32;1m[+] Found hash in {infile} and saved it in {output}\033[0m')


def main():
    # args
    parser = argparse.ArgumentParser(description="StegoCracker - easy way to crack steganography")

    parser.add_argument('file', help='A file to search for hidden message')
    parser.add_argument('-o', '--output', default="temp", help='Full path for folder for found messages')
    parser.add_argument('-p', action='store_true', help='Use this flag if you want to crack a steghide password')
    parser.add_argument('-w', '--wordlist', required=False, help='A wordlist used to crack a password')

    args = parser.parse_args()

    infile = args.file
    data = getdata(infile)
    output = args.output
    pass_crack_flag = args.p
    wordlist = args.wordlist

    if pass_crack_flag:
        if not find_executable('steghide'):
            print('\033[31;1m[-] "steghide" is not installed. Run "sudo apt install steghide -y" to install '
                  'or if you are using Windows like Kacper then lol\033[0m')
            exit()

        if not os.path.isfile(wordlist):
            print(f'\033[31;1m[-] Wordlist {wordlist} does not exist!\033[0m')
            exit()

        print('\033[34;1m[i] Cracking file with password method...\033[0m')
        password_cracker = PasswordCracker(infile, wordlist)
        password_cracker.run()

    else:
        print('\033[34;1m[i] Bruteforcing all possible file types...\033[0m')
        if not os.path.isdir(output):
            print(f'\033[34;1m[i] Creating directory {output}\033[0m')
            os.mkdir(output)
        Thread(target=jpg, args=(infile, data, output,)).start()
        Thread(target=pdf, args=(infile, data, output,)).start()
        Thread(target=exe, args=(infile, data, output,)).start()
        Thread(target=txt_hash, args=(infile, data, output,)).start()


if __name__ == '__main__':
    main()
