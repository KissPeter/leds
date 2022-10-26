import os
from typing import Tuple

from dataclasses import dataclass


class BaseDataClass:
    def get_values(self):
        """
        :rtype: tuple
        """
        return tuple(self.__dict__.values())


@dataclass
class Colors(BaseDataClass):
    red: Tuple = (255, 0, 0)
    blue: Tuple = (0, 255, 0)
    green: Tuple = (0, 0, 255)


@dataclass
class Container:
    led_id: int
    gpio: int = os.getenv("GPIO", 5)


DEFAULT_COLOR = Colors.red
status_id_to_color = {4: Colors.green}

contaiener_data = {
    "a1": Container(led_id=0, gpio=5),
    "a2": Container(led_id=1, gpio=5),
    "a3": Container(led_id=2, gpio=5),
    "a4": Container(led_id=3, gpio=5),
    "a5": Container(led_id=4, gpio=5),
    "a6": Container(led_id=5, gpio=5),
    "a7": Container(led_id=6, gpio=5),
    "a8": Container(led_id=7, gpio=5),
    "a9": Container(led_id=8, gpio=5),
    "a10": Container(led_id=9, gpio=5),
    "a11": Container(led_id=10, gpio=5),
    "a12": Container(led_id=11, gpio=5),
    "a13": Container(led_id=12, gpio=5),
    "a14": Container(led_id=13, gpio=5),
    "a15": Container(led_id=14, gpio=5),
    "a16": Container(led_id=15, gpio=5),
    "a17": Container(led_id=16, gpio=5),
    "a18": Container(led_id=17, gpio=5),
    "a19": Container(led_id=18, gpio=5),
    "a20": Container(led_id=19, gpio=5),
    "a21": Container(led_id=20, gpio=5),
    "a22": Container(led_id=21, gpio=5),
    "a23": Container(led_id=22, gpio=5),
    "a24": Container(led_id=23, gpio=5),
    "a25": Container(led_id=24, gpio=5),
    "a26": Container(led_id=25, gpio=5),
    "a27": Container(led_id=26, gpio=5),
    "a28": Container(led_id=27, gpio=5),
    "a29": Container(led_id=28, gpio=5),
    "a30": Container(led_id=29, gpio=5),
    "a31": Container(led_id=30, gpio=5),
    "a32": Container(led_id=31, gpio=5),
    "a33": Container(led_id=32, gpio=5),
    "a34": Container(led_id=33, gpio=5),
    "a35": Container(led_id=34, gpio=5),
    "a36": Container(led_id=35, gpio=5),
    "a37": Container(led_id=36, gpio=5),
    "a38": Container(led_id=37, gpio=5),
    "a39": Container(led_id=38, gpio=5),
    "a40": Container(led_id=39, gpio=5),
    "a41": Container(led_id=40, gpio=5),
    "a42": Container(led_id=41, gpio=5),
    "a43": Container(led_id=42, gpio=5),
    "a44": Container(led_id=43, gpio=5),
    "a45": Container(led_id=44, gpio=5),
    "a46": Container(led_id=45, gpio=5),
    "a47": Container(led_id=46, gpio=5),
    "a48": Container(led_id=47, gpio=5),
    "a49": Container(led_id=48, gpio=5),
    "a50": Container(led_id=49, gpio=5),
    "b1": Container(led_id=50, gpio=5),
    "b2": Container(led_id=51, gpio=5),
    "b3": Container(led_id=52, gpio=5),
    "b4": Container(led_id=53, gpio=5),
    "b5": Container(led_id=54, gpio=5),
    "b6": Container(led_id=55, gpio=5),
    "b7": Container(led_id=56, gpio=5),
    "b8": Container(led_id=57, gpio=5),
    "b9": Container(led_id=58, gpio=5),
    "b10": Container(led_id=59, gpio=5),
    "b11": Container(led_id=60, gpio=5),
    "b12": Container(led_id=61, gpio=5),
    "b13": Container(led_id=62, gpio=5),
    "b14": Container(led_id=63, gpio=5),
    "b15": Container(led_id=64, gpio=5),
    "b16": Container(led_id=65, gpio=5),
    "b17": Container(led_id=66, gpio=5),
    "b18": Container(led_id=67, gpio=5),
    "b19": Container(led_id=68, gpio=5),
    "b20": Container(led_id=69, gpio=5),
    "b21": Container(led_id=70, gpio=5),
    "b22": Container(led_id=71, gpio=5),
    "b23": Container(led_id=72, gpio=5),
    "b24": Container(led_id=73, gpio=5),
    "b25": Container(led_id=74, gpio=5),
    "b26": Container(led_id=75, gpio=5),
    "b27": Container(led_id=76, gpio=5),
    "b28": Container(led_id=77, gpio=5),
    "b29": Container(led_id=78, gpio=5),
    "b30": Container(led_id=79, gpio=5),
    "b31": Container(led_id=80, gpio=5),
    "b32": Container(led_id=81, gpio=5),
    "b33": Container(led_id=82, gpio=5),
    "b34": Container(led_id=83, gpio=5),
    "b35": Container(led_id=84, gpio=5),
    "b36": Container(led_id=85, gpio=5),
    "b37": Container(led_id=86, gpio=5),
    "b38": Container(led_id=87, gpio=5),
    "b39": Container(led_id=88, gpio=5),
    "b40": Container(led_id=89, gpio=5),
    "b41": Container(led_id=90, gpio=5),
    "b42": Container(led_id=91, gpio=5),
    "b43": Container(led_id=92, gpio=5),
    "b44": Container(led_id=93, gpio=5),
    "b45": Container(led_id=94, gpio=5),
    "b46": Container(led_id=95, gpio=5),
    "b47": Container(led_id=96, gpio=5),
    "b48": Container(led_id=97, gpio=5),
    "b49": Container(led_id=98, gpio=5),
    "b50": Container(led_id=99, gpio=5),
}
