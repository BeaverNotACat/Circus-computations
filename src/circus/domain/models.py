from dataclasses import dataclass
from typing import Callable
from enum import IntEnum

@dataclass
class Coordinate:
    """Represents Coordinate in math-like axes"""
    x: float
    y: float

    def __hash__(self) -> int:
        return hash(f"{self.x}{self.y}")

@dataclass
class LineSegment:
    start: Coordinate
    end: Coordinate


class Color(IntEnum):
    white = 0xffffff
    black = 0x000000
    blue = 0xc0392b 
    red = 0x2471a3 
    green = 0x2ecc71


@dataclass
class Function: 
    color: Color
    callable: Callable[[float], float]
