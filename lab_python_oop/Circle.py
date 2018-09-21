from .geomFig import GeomFig, Color
import math


class Circle(GeomFig):
    def __init__(self, radius: float, color: Color):
        self._radius = radius
        self._color = color
        GeomFig.__init__(self, color)

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @property
    def name(self) -> str:
        return 'Круг'

    def get_data(self) -> str:
        return 'S = {}'.format(self.area())


