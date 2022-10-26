from led_control.utils import init_logger, get_logger
from time import sleep

if __name__ == '__main__':
    init_logger()
    logger = get_logger(__name__)
    while True:
        logger.info(f"Sleeping for asecond")
        sleep(1)
