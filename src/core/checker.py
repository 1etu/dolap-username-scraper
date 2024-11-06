import requests
import time
from bs4 import BeautifulSoup
from typing import Optional
from colorama import Fore, Style
from src.config.settings import HEADERS, DEFAULT_BASE_URL, DEFAULT_MAX_WORKERS, DEFAULT_DELAY

class ProfileChecker:
    def __init__(self, base_url: str = DEFAULT_BASE_URL, max_workers: int = DEFAULT_MAX_WORKERS, delay: int = DEFAULT_DELAY):
        self.base_url = base_url
        self.max_workers = max_workers
        self.delay = delay
        self.headers = HEADERS

    def check_username(self, username: str) -> Optional[str]:
        start_time = time.time()
        url = f"{self.base_url}/profil/{username}"
        
        try:
            response = requests.get(url, headers=self.headers, allow_redirects=True)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if response.url != url:
                return None
                
            profile_indicators = [
                soup.find('div', class_='person-img'),
            ]
            
            exists = any(indicator is not None for indicator in profile_indicators)
            
            elapsed_time = time.time() - start_time
            if exists:
                print(f"{Fore.RED}[-] Not Available: {username} {Style.DIM}({elapsed_time:.2f}s){Style.RESET_ALL}")
                return username
            else:
                print(f"{Fore.GREEN}[+] Available: {username} {Style.DIM}({elapsed_time:.2f}s){Style.RESET_ALL}")
                return None
                
        except requests.RequestException as e:
            print(f"{Fore.YELLOW}[!] Error checking {username}: {str(e)}{Style.RESET_ALL}")
            return None
        
        finally:
            time.sleep(self.delay)
