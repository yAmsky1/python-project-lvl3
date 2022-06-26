import os
from urllib.parse import urlparse


def get_file_name(url):
    draft_name, ext = process_url(url)
    name = format_file_name(draft_name, ext)
    return name


def process_url(url):

    if urlparse(url).path:
        name, ext = os.path.splitext(urlparse(url).netloc + urlparse(url).path)
        return name, ext

    else:
        name, ext = os.path.splitext(urlparse(url).netloc)
        return name, ext


def format_file_name(file_name, ext):
    if not ext:
        ext = '.html'
    for symbol in file_name:
        if not symbol.isalnum():
            file_name = file_name.replace(symbol, '-')
    if file_name.endswith('-'):
        file_name = file_name[:-1]
    return file_name + ext
