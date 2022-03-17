"""
In main script there will be implemented multithreading and option parser for different crack methods
"""
import argparse
import os
from distutils.spawn import find_executable

from cracker import crack_password


def main():
    parser = argparse.ArgumentParser(description="StegoCracker - easy way to crack steganography")

    parser.add_argument('file', help='A file to crack')
    parser.add_argument('-m', '--method', help='Cracking method - "password", "lsb", "html"')
    parser.add_argument('-w', '--wordlist', default=None, help='A wordlist file to be used in cracking')
    parser.add_argument('-o', '--output', default=None, help='A output file for cracking')

    args = parser.parse_args()

    file_path = args.file
    method = args.method
    wordlist_path = args.wordlist
    output = args.output or file_path + '.out'

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

        print('[i] Cracking file with password method')
        crack_password(file_path, wordlist_path, output)

    elif method == 'lsb':
        print('[i] Cracking file with lsb method')

    elif method == 'html':
        print('[i] Cracking file with html method')

    else:
        print('\033[31;1m[-] Wrong cracking method specified. Possible methods - "password", "lsb", "html"\033[0m')


if __name__ == '__main__':
    main()
