from colorama import init
from src.core.checker import ProfileChecker
from src.core.generator import UsernameGenerator
from src.core.scraper import ProfileScraper
from src.utils.cli import parse_args

init()

def main():
    args = parse_args()
    
    checker = ProfileChecker(max_workers=args.workers, delay=args.delay)
    generator = UsernameGenerator()
    scraper = ProfileScraper(checker)
    
    if args.file:
        usernames = generator.read_from_file(args.file)
    else:
        usernames = generator.generate_combinations(args.letters)
    
    scraper.run(usernames, args.output)

if __name__ == "__main__":
    main() 