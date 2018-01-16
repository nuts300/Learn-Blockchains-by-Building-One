# -*- Coding: UTF-8 -*-
import logging


def get_logger(name):

    logger = logging.getLogger(name)
    stream_header = logging.StreamHandler()

    if stream_header:
        logger.addHandler(stream_header)
    logger.setLevel(logging.DEBUG)

    return logger
