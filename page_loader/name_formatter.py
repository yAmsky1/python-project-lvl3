import os
from urllib.parse import urlparse


def get_name(url, directory=False):
    draft_name, ext = process_url(url)
    if directory:
        return format_name(draft_name, directory=True)
    return format_name(draft_name, ext=ext)


def process_url(url):

    if urlparse(url).path:
        name, ext = os.path.splitext(urlparse(url).netloc + urlparse(url).path)
        return name, ext

    else:
        name = urlparse(url).netloc
        ext = None
        return name, ext


def format_name(name, ext=None, directory=False):
    if not ext:
        ext = '.html'
    for symbol in name:
        if not symbol.isalnum():
            name = name.replace(symbol, '-')
    if name.endswith('-'):
        name = name[:-1]
    if directory:
        return name + '_files'
    return name + ext
