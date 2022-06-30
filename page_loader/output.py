import os
from page_loader.logger import set_n_get_logger


logger = set_n_get_logger(__name__)


def save_as_file(data, path, tag=None):
    logger.info(f"Start downloading {tag}")
    if tag == 'img':
        with open(path, 'wb') as file:
            file.write(data.content)

    elif tag == 'html':
        with open(path, 'w') as file:
            file.write(data)

    else:
        with open(path, 'w') as file:
            file.write(data.text)

    logger.info(f"{tag} has been loaded into")

    return


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        logger.info(f'Directory {path} has been created')
