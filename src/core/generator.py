import string
import itertools
from typing import List
from colorama import Fore, Style

class UsernameGenerator:
    @staticmethod
    def generate_combinations(length: int) -> List[str]:
        chars = string.ascii_lowercase + string.digits
        return [''.join(combo) for combo in itertools.product(chars, repeat=length)]

    @staticmethod
    def read_from_file(filename: str) -> List[str]:
        try:
            with open(filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"{Fore.RED}[!] Error: File {filename} not found{Style.RESET_ALL}")
            exit(1)
