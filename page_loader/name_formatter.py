from urllib.parse import urlparse


EXT = '.html'


def process_url(url):
    if urlparse(url).path:
        file_name = urlparse(url).netloc + urlparse(url).path
        return file_name
    else:
        file_name = urlparse(url).netloc
        return file_name


def format_file_name(file_name):
    for symbol in file_name:
        if not symbol.isalnum():
            file_name = file_name.replace(symbol, '-')
    if file_name.endswith('-'):
        file_name = file_name[:-1]
    return file_name + EXT
