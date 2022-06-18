import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('page_url', type=str)
    parser.add_argument(
        "-o", "--output",
        help='Set the path to directory',
        default=os.getcwd()
    )
    args = parser.parse_args()


if __name__ == '__main__':
    main()
