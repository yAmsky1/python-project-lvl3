import logging


fmt = '[%(asctime)s %(levelname)s]:%(message)s'


def cfd_and_get_logger(name=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    info_handler = logging.FileHandler('.logs.log')
    info_handler.setLevel(logging.INFO)
    error_handler = logging.StreamHandler()
    error_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(fmt=fmt)
    info_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    return logger
