from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urljoin, urlparse, urlunparse
from page_loader.name_formatter import get_name
from page_loader.logger import set_n_get_logger


TAGS_ATTRIBUTES = {
    'img': 'src',
    'script': 'src',
    'link': 'href'
}


logger = set_n_get_logger(__name__)


def make_parser(html_page):
    return BeautifulSoup(html_page, 'lxml')


def parse_(files_dir_path, base_url):
    try:
        html_ = requests.get(base_url)
        parser = make_parser(html_.text)
        resources_paths = parser.find_all(list(TAGS_ATTRIBUTES.keys()))
        resources = get_resources(resources_paths, files_dir_path, base_url)
        html_page = parser.prettify()

    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema) as e:
        logger.error('WRONG ADDRESS! Check URL-address')
        raise Exception('WRONG ADDRESS!') from e

    except requests.exceptions.HTTPError as e:
        logger.error('CONNECTION ERROR! Check URL-address')
        raise Exception('CONNECTION ERROR!') from e

    except requests.exceptions.ConnectionError as e:
        logger.error('CONNECTION ERROR! Check URL-address')
        raise Exception('CONNECTION ERROR!') from e

    return resources, html_page


def get_resources(resources_paths, files_dir_path, base_url):
    resources = []
    parsed_base_url = urlparse(base_url)
    for tag in resources_paths:
        full_resource_url = ''
        attribute = TAGS_ATTRIBUTES.get(tag.name)
        resource_url = tag.get(attribute)
        parsed_resource_url = urlparse(resource_url)

        if not parsed_resource_url.netloc:
            full_resource_url = urljoin(base_url, resource_url)

        if parsed_resource_url.netloc == parsed_base_url.netloc:

            if parsed_resource_url.scheme:
                url_scheme = parsed_resource_url.scheme

            else:
                url_scheme = parsed_base_url.scheme

            url_netloc = parsed_resource_url.netloc
            url_path = parsed_resource_url.path
            url_query = parsed_resource_url.query
            url_fragment = parsed_resource_url.fragment
            full_resource_url = urlunparse(
                (
                    url_scheme,
                    url_netloc,
                    url_path,
                    "",
                    url_query,
                    url_fragment
                )
            )

        if not full_resource_url:
            continue

        resource_file_name = get_name(full_resource_url)
        new_resource_path = os.path.join(
            os.path.basename(files_dir_path),
            resource_file_name
        )
        tag[attribute] = new_resource_path
        resource_file_path = os.path.join(files_dir_path, resource_file_name)
        resources.append((full_resource_url, resource_file_path, tag.name))

    return resources
