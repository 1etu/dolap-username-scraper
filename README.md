## Installation

```bash
git clone https://github.com/1etu/dolap-username-scraper
cd dolap-username-checker
pip install requests beautifulsoup4 colorama
```

## Usage

## 1. Check usernames from file
```bash
python -m src.main --file path/to/usernames.txt
```

## 2. Generate and check usernames
```bash
python -m src.main --letters 3
```

## Command Line (CLI) Options:
| Option | Description | Default |
|--------|-------------|---------|
| --file | Input file containing usernames (one per line) | Required |
| --letters | Generate usernames of specified length | Required |
| --output | Output file path for results | output.txt |
| --workers | Number of concurrent worker threads | 3 |
| --delay | Delay between requests in seconds | 1 |
\* Either --file or --letters must be specified, but not both.

## Examples
## Check usernames from a file with custom output:
```bash
python -m src.main --file usernames.txt --output results.txt
```

## Generate 4-letter usernames with 5 concurrent workers:
```bash
python -m src.main --letters 4 --workers 5
```

## Check usernames with increased delay between requests:
```bash
python -m src.main --file usernames.txt --delay 2
```



