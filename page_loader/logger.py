import logging


def set_n_get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('.log.txt', 'w')
    logger.addHandler(file_handler)
    return logger


def set_logger_config():
    return logging.basicConfig(level=logging.INFO)
