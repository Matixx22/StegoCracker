from getdata import icmp_get_data
from getdata import image_get_lsb
from getdata import html_get_lower_letters
from getdata import html_get_upper_letters

from checkdata import check_hash
from checkdata import check_jpg
from checkdata import check_pdf
from checkdata import check_txt

import argparse
import os
from distutils.spawn import find_executable

from cracker import PasswordCracker

"""
In main script there will be implemented multithreading and option parser for different crack methods
"""

"""
But for now it's showing how to use getdata and checkdata packages
"""

def find_steg(source):
    find_hash = check_hash(source)
    if find_hash[0]:
        print("Found Hash " + find_hash[1])
        return "Found Hash " + find_hash[1]

    find_jpg = check_jpg(source)
    if find_jpg[0]:
        print("Found JPG. New file location: " + find_jpg[1])
        return "Found JPG. New file location: " + find_jpg[1]

    find_pdf = check_pdf(source)
    if find_pdf[0]:
        print("Found PDF. New file location: " + find_pdf[1])
        return "Found PDF. New file location: " + find_pdf[1]

    find_txt = check_txt(source)
    if find_txt[0]:
        print("Found text: " + find_txt[1])
        return "Found text: " + find_txt[1]

def main():
    parser = argparse.ArgumentParser(description="StegoCracker - easy way to crack steganography")

    parser.add_argument('file', help='A file to crack')
    parser.add_argument('-m', '--method', help='Cracking method - "password", "lsb", "html"')
    parser.add_argument('-w', '--wordlist', default=None, help='A wordlist file to be used in cracking')
    parser.add_argument('-o', '--output', default=None, help='A output file for cracking')
    parser.add_argument('-t', '--threads', default=None, type=int, help='Number of threads (default 8)')

    args = parser.parse_args()

    file_path = args.file
    method = args.method
    wordlist_path = args.wordlist
    output = args.output or file_path + '.out'
    threads = args.threads or 8

    if not os.path.isfile(file_path):
        print(f'\033[31;1m[-] File {file_path} does not exist!\033[0m')
        exit()

    if method is None:
        print('\033[31;1m[-] You must specify a cracking method!\033[0m')
        exit()

    if method == 'password':
        if not find_executable('steghide'):
            print('\033[31;1m[-] "steghide" is not installed. Run "sudo apt install steghide -y to install"\033[0m')
            exit()

        if not os.path.isfile(wordlist_path):
            print(f'\033[31;1m[-] Wordlist {wordlist_path} does not exist!\033[0m')
            exit()

        print('[i] Cracking file with password method...')
        password_cracker = PasswordCracker(file_path, wordlist_path, output, threads)
        password_cracker.run()

    elif method == 'lsb':
        print('[i] Cracking file with lsb method')

    elif method == 'html':
        print('[i] Cracking file with html method')

    else:
        print('\033[31;1m[-] Wrong cracking method specified. Possible methods - "password", "lsb", "html"\033[0m')


if __name__ == '__main__':
    main()
    # html_filename = "./example.html"
    # pcap_filename = "./example.pcap"
    # img_filename = "./example.jpg"
    #
    # find_steg(html_get_lower_letters(html_filename))
    # find_steg(html_get_upper_letters(html_filename))
    # find_steg(icmp_get_data(pcap_filename))
    # find_steg(image_get_lsb(img_filename))
