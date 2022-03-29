"""
This file will contain the main brute force loop. Each cracking method will be in different function.
"""
from subprocess import DEVNULL, run


def crack_password(file, wordlist):
    with open(wordlist, 'r') as wl:
        for password in wl:
            print('Trying passphrase:', password.strip())
            p = run(['steghide', 'extract', '-sf', file, '-xf', '../resources/out', '-p', password.strip(), '-f'],
                    stderr=DEVNULL)

            if p.returncode == 0:
                print('Found passphrase:', password)
                break


