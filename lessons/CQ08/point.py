"""Create a class name is Point."""

from __future__ import annotations


__author__: str = "730520183"


class Point:
    """Class Point with two attributes x and y."""
    x: float
    y: float
    
    def __init__(self, x_init: float, y_init: float) -> None: 
        """The value of attributes in Point should be x,y_init."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None: 
        """Modify the original class."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Without modify the orginal class and return a new list as Point."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)