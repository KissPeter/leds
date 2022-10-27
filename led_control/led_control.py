import os

import machine
import neopixel
from typing import Union, Tuple

from led_control.dataclasses import (
    contaiener_data,
    DEFAULT_COLOR,
    status_id_to_color,
    Colors,
)
from led_control.exceptions import BaseValidationException
from led_control.utils import LoggingClass


class LEDControl(LoggingClass):
    def __init__(self):
        super().__init__()
        self.GPIO = os.getenv("GPIO", 5)
        self._init_neopixel()

    def _init_neopixel(self):
        self.neopixel = neopixel.NeoPixel(
            machine.Pin(self.GPIO), n=len(contaiener_data), auto_write=True
        )

    def _get_led_id_from_container(self, container: str) -> int:
        _cont_data = contaiener_data.get(container)
        if not _cont_data:
            self.logger.error(f"No data for {container}")
        return _cont_data.led_id

    def _check_set_gpio(self, container: str):
        """
        This way we support multiple LED strips on multiple GPIO pins, just update container_data
        """
        _cont_data = contaiener_data.get(container)
        if self.GPIO != _cont_data.gpio:
            self.GPIO = _cont_data.gpio
            self._init_neopixel()

    @staticmethod
    def _get_color_from_status_id(status_id: int) -> Union[Tuple, Colors]:
        return status_id_to_color.get(status_id, DEFAULT_COLOR)

    def set_status(self, container: str, status_id: int):
        if container not in contaiener_data.keys():
            raise BaseValidationException(f"unknown container: {container}")
        self._check_set_gpio()
        _led_id = self._get_led_id_from_container()
        _color = self._get_color_from_status_id(status_id)
        self.logger.info(f"Set {container} (LED: {_led_id}) to {_color}")
        self.neopixel[_led_id] = _color
