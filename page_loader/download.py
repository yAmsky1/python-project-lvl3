import requests
import os
from page_loader.name_formatter import get_name
from page_loader.output import create_directory, save_as_file
from page_loader.html_parser import parse_
from page_loader.logger import cfd_and_get_logger
from progress.bar import ChargingBar


logger = cfd_and_get_logger(__name__)


def download(base_url, output_path):
    if not os.path.exists(output_path):
        logger.error('output directory %s does not exist!', output_path)
        raise IOError('output directory does not exist!')
    logger.info('start page download from %s', base_url)
    page_file_name = get_name(base_url)
    page_output_path = os.path.join(output_path, page_file_name)
    file_dir_name = get_name(base_url, directory=True)
    files_dir_path = os.path.join(output_path, file_dir_name)
    resources, html_page = parse_(files_dir_path, base_url)

    if resources:
        create_directory(files_dir_path)
        download_resources(resources)

    save_as_file(html_page, page_output_path, tag='html')
    logger.info("page and resources from %s has been loaded", base_url)
    return page_output_path


def download_resources(resources):

    progress = ChargingBar('downloading resources...', max=len(resources))

    for resource_url, resource_path, tag in resources:
        progress.next()
        resource = requests.get(resource_url)
        save_as_file(resource, resource_path, tag)

    progress.finish()
