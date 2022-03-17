"""
This file will contain the main brute force loop. Each cracking method will be in different function.
"""
from subprocess import DEVNULL, run


def crack_password(file, wordlist, output):
    with open(wordlist, 'r') as wl:
        for password in wl:
            password = password.strip()
            p = run(['steghide', 'extract', '-sf', file, '-xf', output, '-p', password, '-f'],
                    stderr=DEVNULL)

            if p.returncode == 0:
                print(f'\033[32;1m[+] Found passphrase: {password}\033[0m')
                print('[+] Output is in file:', output)
                break


