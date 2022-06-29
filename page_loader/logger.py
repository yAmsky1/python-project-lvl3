import logging
import sys


def set_n_get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    file_handler = logging.FileHandler('.log.txt')
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)
    return logger


def set_logger_config():
    return logging.basicConfig(level=logging.INFO)
