from led_control.utils import init_logger, get_logger
from led_control.container_manager import Container
from time import sleep


def main():
    logger = get_logger(__name__)
    containers = Container()
    containers.init_leds()
    while True:
        logger.info(f"Sleeping for asecond")
        containers.query_and_update_states()
        sleep(1)


if __name__ == "__main__":
    init_logger()
    main()
