"""
This file will contain the main brute force loop. Each cracking method will be in different function.
"""
from queue import Queue
from subprocess import DEVNULL, run
from threading import Thread


class PasswordCracker:
    def __init__(self, file, wordlist, output, threads):
        self.file = file
        self.wordlist = wordlist
        self.output = output
        self.threads = threads
        self.passwords = Queue()
        self.iter = 0

        with open(wordlist) as wl:
            for password in wl:
                self.passwords.put(password.strip())

        self.passwords_len = self.passwords.qsize()

    def _crack(self):
        while not self.passwords.empty():
            password = self.passwords.get()

            print(f'\r[i] Progress: {self.iter}/{self.passwords_len} ({round(self.iter / self.passwords_len * 100, 2)}%)', end='')

            p = run(['steghide', 'extract', '-sf', self.file, '-xf', self.output, '-p', password, '-f'], stderr=DEVNULL)

            self.iter += 1

            if p.returncode == 0:
                print(f'\n\033[32;1m[+] Found passphrase: {password}\033[0m')
                print('[+] Output is in file:', self.output)
                with self.passwords.mutex:
                    self.passwords.queue.clear()
                return

    def run(self):
        threads = []
        for _ in range(self.threads):
            thread = Thread(target=self._crack, daemon=True)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
