from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urljoin
from page_loader.name_formatter import get_file_name


def make_parser(html_page):
    return BeautifulSoup(html_page, 'lxml')


def parse_(files_dir_path, base_url):
    html_ = requests.get(base_url).content
    parser = make_parser(html_)
    images_src = parser.find_all('img')
    images = get_images(images_src, files_dir_path, base_url)
    html_page = parser.prettify()
    return images, html_page


def get_images(images_src, files_dir_path, base_url):
    images = []

    for image in images_src:
        image_src = image.get('src')
        image_url = urljoin(base_url, image_src)
        image_file_name = get_file_name(image_url)
        new_image_src = os.path.join(
            os.path.basename(files_dir_path),
            image_file_name
        )
        image['src'] = new_image_src
        image_path = os.path.join(files_dir_path, image_file_name)
        images.append((image_url, image_path))

    return images
