import requests
import os
from page_loader.name_formatter import get_file_name, get_directory_name
from page_loader.file_saver import create_directory, save_as_file, \
    save_html_page
from page_loader.loader import load_page
from page_loader.html_parser import parse_html_page
from page_loader.logger import cfg_and_get_logger
from progress.bar import ChargingBar


logger = cfg_and_get_logger(__name__)


def download(base_url, output_path):
    if not os.path.exists(output_path):
        logger.error('output directory %s does not exist!', output_path)
        raise IOError('output directory does not exist!')
    logger.info('start page download from %s', base_url)
    page_file_name = get_file_name(base_url)
    page_output_path = os.path.join(output_path, page_file_name)
    file_dir_name = get_directory_name(page_file_name)
    files_dir_path = os.path.join(output_path, file_dir_name)
    page = load_page(base_url)
    resources, html_page = parse_html_page(page, files_dir_path, base_url)

    if resources:
        create_directory(files_dir_path)
        download_resources(resources)

    save_html_page(html_page, page_output_path)
    logger.info("page and resources from %s has been loaded", base_url)
    return page_output_path


def download_resources(resources):
    progress = ChargingBar('downloading resources...', max=len(resources))

    for resource_url, resource_path in resources:
        progress.next()
        resource = requests.get(resource_url)
        save_as_file(resource, resource_path)

    progress.finish()
