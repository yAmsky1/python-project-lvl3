import requests
from page_loader.logger import get_logger


logger = get_logger(__name__)


def load_content(url):
    response = load(url)
    return response.content


def load_text(url):
    response = load(url)
    return response.text


def load(url):
    try:
        logger.info('trying to connect')
        response = requests.get(url)
        response.raise_for_status()
        logger.info('successful connection')

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

    else:
        return response
