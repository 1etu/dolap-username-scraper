import time
from datetime import datetime
from typing import List
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style
from .checker import ProfileChecker

class ProfileScraper:
    def __init__(self, checker: ProfileChecker):
        self.checker = checker
        
    def run(self, usernames: List[str], output_file: str) -> None:
        start_time = time.time()
        total_usernames = len(usernames)
        
        print(f"{Back.BLUE}{Fore.WHITE} Starting scan of {total_usernames} usernames {Style.RESET_ALL}")
        
        with ThreadPoolExecutor(max_workers=self.checker.max_workers) as executor:
            results = list(executor.map(self.checker.check_username, usernames))
        
        non_existing_profiles = [usernames[i] for i, result in enumerate(results) if result is None]
        
        with open(output_file, 'w') as f:
            f.write(f"# Scan completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Found {total_usernames - len(non_existing_profiles)} profiles out of {total_usernames} checked\n")
            f.write(f"# {len(non_existing_profiles)} usernames not found:\n\n")
            for username in non_existing_profiles:
                f.write(f"{username}\n")
        
        elapsed_time = time.time() - start_time
        print(f"\n{Back.GREEN}{Fore.BLACK} Scan Complete {Style.RESET_ALL}")
        print(f"Found {Fore.GREEN}{total_usernames - len(non_existing_profiles)}{Style.RESET_ALL} profiles")
        print(f"Total time: {Fore.CYAN}{elapsed_time:.2f}s{Style.RESET_ALL}")
        print(f"Results saved to: {Fore.CYAN}{output_file}{Style.RESET_ALL}")
