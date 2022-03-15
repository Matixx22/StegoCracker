"""
In main script there will be implemented multithreading and option parser for different crack methods
"""
import argparse


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="StegoCracker - easy way to crack steganography")
    args = parser.parse_args()
