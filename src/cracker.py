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

        with open(wordlist) as wl:
            for password in wl:
                self.passwords.put(password.strip())

    def _crack(self, id):
        while not self.passwords.empty():
            password = self.passwords.get()

            # print(f'Thread {id} tried password {password}')

            p = run(['steghide', 'extract', '-sf', self.file, '-xf', self.output, '-p', password, '-f'], stderr=DEVNULL)

            if p.returncode == 0:
                print(f'\033[32;1m[+] Found passphrase: {password}\033[0m')
                print('[+] Output is in file:', self.output)
                with self.passwords.mutex:
                    self.passwords.queue.clear()
                return

    def run(self):
        threads = []
        for _ in range(self.threads):
            thread = Thread(target=self._crack, args=(_,), daemon=True)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
