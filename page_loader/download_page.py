import requests
import os
from page_loader.name_formatter import get_file_name
from page_loader.file_saver import save_page_as_file,\
    create_directory, save_sources_as_file
from page_loader.html_parser import parse_


def download_page(url, path=os.getcwd()):
    file_name = get_file_name(url)
    file_path = os.path.join(path, file_name)
    files_dir_path = create_directory(file_path)
    images, html_page = parse_(files_dir_path, url)
    save_page_as_file(html_page, file_path)
    if images:
        for image_url, image_path in images:
            image = requests.get(image_url).content
            save_sources_as_file(image, image_path)

    return file_path
