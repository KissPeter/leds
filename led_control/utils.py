import logging
import os
import sys
from logging import Logger
PROJECT = "ROBILEDS"


def init_logger():
    """
    Setup logger which can be used later with the get_logger method
    :return:
    """
    logger = logging.getLogger(PROJECT)
    if not logger.hasHandlers():
        log_handler = logging.StreamHandler(stream=sys.stdout)
        log_handler.setFormatter(
            logging.Formatter("[%(levelname)s][%(funcName)20s()] %(name)s: %(message)s")
        )
        logger.addHandler(log_handler)
    logger.setLevel(os.getenv("LOG_LEVEL", "DEBUG").upper())


def get_logger(name: str) -> Logger:
    """
    Configure child logger
    """
    return logging.getLogger(PROJECT).getChild(name)

