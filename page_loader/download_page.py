import requests
import os
from page_loader.name_formatter import process_url, format_file_name
from page_loader.file_saver import write_data_to_file


def download_page(url, path=os.getcwd()):
    file_name = process_url(url)
    formatted_name = format_file_name(file_name)
    file_path = os.path.join(path, formatted_name)
    response = requests.get(url)
    write_data_to_file(response, file_path)
    return file_path
