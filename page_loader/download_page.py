import requests
import os
from urllib.parse import urlparse


EXT = '.html'


def download_page(url, path=os.getcwd()):
    file_name = process_url(url)
    formatted_name = format_file_name(file_name)
    file_path = os.path.join(path, formatted_name)
    response = requests.get(url)
    write_data_to_file(response, file_path)
    return file_path


def process_url(url):
    if urlparse(url).path:
        file_name = urlparse(url).netloc + urlparse(url).path
        return file_name
    else:
        return urlparse(url).netloc


def format_file_name(file_name):
    for symbol in file_name:
        if not symbol.isalnum():
            file_name = file_name.replace(symbol, '-')
    if file_name.endswith('-'):
        file_name = file_name[:-1]
    return file_name + EXT


def write_data_to_file(data, path):
    with open(path, 'wb') as file:
        file.write(data.content)
    return
