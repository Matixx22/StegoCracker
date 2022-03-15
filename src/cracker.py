"""
This file will contain the main brute force loop. Each cracking method will be in different function.
"""


def crack_password(file, wordlist):
    with open(wordlist, 'r') as wl:
        password = wl.readline()
