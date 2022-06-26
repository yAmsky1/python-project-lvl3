import requests
import os
from page_loader.name_formatter import get_file_name
from page_loader.output import create_directory, save_as_file
from page_loader.html_parser import parse_


def download_page(url, path=os.getcwd()):
    file_name = get_file_name(url)
    file_path = os.path.join(path, file_name)
    files_dir_path = create_directory(file_path)
    resources, html_page = parse_(files_dir_path, url)
    save_as_file(html_page, file_path)
    if resources:
        for resource_url, resource_path in resources:
            _, file_ext = os.path.splitext(resource_path)
            if file_ext in ['.jpg', '.jpeg', '.png']:
                resource = requests.get(resource_url).content
                save_as_file(resource, resource_path)
            else:
                resource = requests.get(resource_url).text
                save_as_file(resource, resource_path)

    return file_path
