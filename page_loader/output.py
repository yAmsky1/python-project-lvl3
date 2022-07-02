import os
from page_loader.logger import cfd_and_get_logger


logger = cfd_and_get_logger(__name__)


def save_as_file(data, path, tag=None):
    logger.info("start downloading %s", tag)

    if tag == 'img':
        with open(path, 'wb') as file:
            file.write(data.content)

    elif tag == 'html':
        with open(path, 'w') as file:
            file.write(data)

    else:
        with open(path, 'w') as file:
            file.write(data.text)
    logger.info("%s download completed", tag)
    return


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        logger.info('directory has been created')
