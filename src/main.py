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
        print(f'File {file_path} does not exist!')
        exit()

    if method is None:
        print('You must specify a cracking method!')
        exit()

    if not os.path.isfile(wordlist_path):
        print(f'Wordlist {wordlist_path} does not exist!')
        exit()

    if not find_executable('steghide'):
        print('"steghide" is not installed. Run "sudo apt install steghide -y to install"')
        exit()

    if method == 'password':
        print('Cracking file with password method')
        crack_password(file_path, wordlist_path, output)
    elif method == 'lsb':
        print('Cracking file with lsb method')
    elif method == 'html':
        print('Cracking file with html method')
    else:
        print('Wrong cracking method specified. Possible methods - "password", "lsb", "html"')


if __name__ == '__main__':
    main()
