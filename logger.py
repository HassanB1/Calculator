import logging


def logger(file_name, item):
    logging.basicConfig(filename=file_name, level=logging.DEBUG)
    logging.info(item)
