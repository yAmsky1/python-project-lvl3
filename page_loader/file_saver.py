import os
from page_loader.logger import cfg_and_get_logger


logger = cfg_and_get_logger(__name__)


def save_as_file(data, path):
    logger.info("start downloading resource into %s", path)

    with open(path, 'wb') as file:
        file.write(data.content)

    logger.info("resource download completed")
    return


def save_html_page(data, path):
    with open(path, 'w') as file:
        file.write(data)


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        logger.info('directory has been created')
