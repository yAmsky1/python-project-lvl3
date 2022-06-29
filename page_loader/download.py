import requests
import os
from page_loader.name_formatter import get_file_name
from page_loader.output import create_directory, save_as_file
from page_loader.html_parser import parse_
from page_loader.logger import set_n_get_logger


IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']


logger = set_n_get_logger(__name__)


def download_page(base_url, path=os.getcwd()):
    page_file_name = get_file_name(base_url)
    page_output_path = os.path.join(path, page_file_name)
    files_dir_path = create_directory(page_output_path)
    resources, html_page = parse_(files_dir_path, base_url)
    save_as_file(html_page, page_output_path)
    logger.info(f"Page from {base_url} has been loaded")

    if resources:
        download_resources(resources, base_url)

    logger.info(f"Page and resources from {base_url} has been loaded")
    return page_output_path


def download_resources(resources, base_url):

    for resource_url, resource_path in resources:
        _, file_ext = os.path.splitext(resource_path)

        if file_ext in IMAGE_EXTENSIONS:
            resource = requests.get(resource_url).content
            save_as_file(resource, resource_path)
            logger.info(f"Image from {base_url} has been loaded")

        else:
            resource = requests.get(resource_url).text
            save_as_file(resource, resource_path)
            logger.info(f"Resource from {base_url} has been loaded")
