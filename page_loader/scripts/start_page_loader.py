#!/usr/bin/env python


import os
import argparse
from page_loader import download_page


def main():
    parser = argparse.ArgumentParser(description='Downloads page')
    parser.add_argument('page_url', type=str)
    parser.add_argument(
        "-o", "--output",
        help='Set the path to directory',
        default=os.getcwd()
    )
    args = parser.parse_args()
    print(download_page(args.page_url, args.output))


if __name__ == '__main__':
    main()
