import os
from typing import Tuple
import board
from adafruit_blinka.board.raspberrypi.raspi_40pin import D18
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
    off: Tuple = (0, 0, 0)


DEFAULT_COLOR = Colors.off
try:
    DEFAULT_PIN = os.getenv("GPIO", D18)
except AttributeError as e:
    print(f"No such pin: {e}.  {board.board_id}")

DB_TABLE = os.getenv("DBTABLE", "budapest_statuses_view")


@dataclass
class Container:
    led_id: int
    gpio: int = DEFAULT_PIN


status_id_to_color = {4: Colors.green, 11: Colors.off}

contaiener_data = {
    "a1": Container(led_id=0),
    "a2": Container(led_id=1),
    "a3": Container(led_id=2),
    "a4": Container(led_id=3),
    "a5": Container(led_id=4),
    "a6": Container(led_id=5),
    "a7": Container(led_id=6),
    "a8": Container(led_id=7),
    "a9": Container(led_id=8),
    "a10": Container(led_id=9),
    "a11": Container(led_id=10),
    "a12": Container(led_id=11),
    "a13": Container(led_id=12),
    "a14": Container(led_id=13),
    "a15": Container(led_id=14),
    "a16": Container(led_id=15),
    "a17": Container(led_id=16),
    "a18": Container(led_id=17),
    "a19": Container(led_id=18),
    "a20": Container(led_id=19),
    "a21": Container(led_id=20),
    "a22": Container(led_id=21),
    "a23": Container(led_id=22),
    "a24": Container(led_id=23),
    "a25": Container(led_id=24),
    "a26": Container(led_id=25),
    "a27": Container(led_id=26),
    "a28": Container(led_id=27),
    "a29": Container(led_id=28),
    "a30": Container(led_id=29),
    "a31": Container(led_id=30),
    "a32": Container(led_id=31),
    "a33": Container(led_id=32),
    "a34": Container(led_id=33),
    "a35": Container(led_id=34),
    "a36": Container(led_id=35),
    "a37": Container(led_id=36),
    "a38": Container(led_id=37),
    "a39": Container(led_id=38),
    "a40": Container(led_id=39),
    "a41": Container(led_id=40),
    "a42": Container(led_id=41),
    "a43": Container(led_id=42),
    "a44": Container(led_id=43),
    "a45": Container(led_id=44),
    "a46": Container(led_id=45),
    "a47": Container(led_id=46),
    "a48": Container(led_id=47),
    "a49": Container(led_id=48),
    "a50": Container(led_id=49),
    "b1": Container(led_id=50),
    "b2": Container(led_id=51),
    "b3": Container(led_id=52),
    "b4": Container(led_id=53),
    "b5": Container(led_id=54),
    "b6": Container(led_id=55),
    "b7": Container(led_id=56),
    "b8": Container(led_id=57),
    "b9": Container(led_id=58),
    "b10": Container(led_id=59),
    "b11": Container(led_id=60),
    "b12": Container(led_id=61),
    "b13": Container(led_id=62),
    "b14": Container(led_id=63),
    "b15": Container(led_id=64),
    "b16": Container(led_id=65),
    "b17": Container(led_id=66),
    "b18": Container(led_id=67),
    "b19": Container(led_id=68),
    "b20": Container(led_id=69),
    "b21": Container(led_id=70),
    "b22": Container(led_id=71),
    "b23": Container(led_id=72),
    "b24": Container(led_id=73),
    "b25": Container(led_id=74),
    "b26": Container(led_id=75),
    "b27": Container(led_id=76),
    "b28": Container(led_id=77),
    "b29": Container(led_id=78),
    "b30": Container(led_id=79),
    "b31": Container(led_id=80),
    "b32": Container(led_id=81),
    "b33": Container(led_id=82),
    "b34": Container(led_id=83),
    "b35": Container(led_id=84),
    "b36": Container(led_id=85),
    "b37": Container(led_id=86),
    "b38": Container(led_id=87),
    "b39": Container(led_id=88),
    "b40": Container(led_id=89),
    "b41": Container(led_id=90),
    "b42": Container(led_id=91),
    "b43": Container(led_id=92),
    "b44": Container(led_id=93),
    "b45": Container(led_id=94),
    "b46": Container(led_id=95),
    "b47": Container(led_id=96),
    "b48": Container(led_id=97),
    "b49": Container(led_id=98),
    "b50": Container(led_id=99),
}


@dataclass
class DBFields(BaseDataClass):
    container: str = "container"
    id: str = "id"
    updated_at: str = "updated_at"
