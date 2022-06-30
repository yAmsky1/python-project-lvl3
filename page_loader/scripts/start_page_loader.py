#!/usr/bin/env python


import sys
import os
import argparse
from page_loader import download_page
from page_loader.logger import set_n_get_logger


logger = set_n_get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Downloads page')
    parser.add_argument('page_url', type=str)
    parser.add_argument(
        "-o", "--output",
        help='Set the path to directory',
        default=os.getcwd()
    )
    args = parser.parse_args()
    try:
        print(download_page(args.page_url, args.output))
    except Exception as e:
        logger.info(e)
        logger.error('Page was not downloaded, see log file')
        sys.exit(1)


if __name__ == '__main__':
    main()
