import argparse
from src.config.settings import DEFAULT_OUTPUT_FILE, DEFAULT_MAX_WORKERS, DEFAULT_DELAY

def parse_args():
    parser = argparse.ArgumentParser(description='Dolap Username Checker')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', type=str, help='Input file containing usernames')
    group.add_argument('--letters', type=int, help='Generate usernames of specified length')
    parser.add_argument('--output', type=str, default=DEFAULT_OUTPUT_FILE, help=f'Output file (default: {DEFAULT_OUTPUT_FILE})')
    parser.add_argument('--workers', type=int, default=DEFAULT_MAX_WORKERS, help=f'Number of worker threads (default: {DEFAULT_MAX_WORKERS})')
    parser.add_argument('--delay', type=int, default=DEFAULT_DELAY, help=f'Delay between requests in seconds (default: {DEFAULT_DELAY})')
    return parser.parse_args()
