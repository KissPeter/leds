from led_control.utils import get_logger


class BaseValidationException(Exception):
    def __init__(
        self,
        error_message,
    ):
        super().__init__()
        self.error_message = error_message
        self.logger = get_logger(self.__class__.__name__)
        self.logger.warning(f"Exception happened {error_message}")
