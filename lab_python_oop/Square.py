from .Rectangle import Rectangle
from .color import Color


class Square(Rectangle):
    def __init__(self, size: float, color: Color):
        Rectangle.__init__(self, size, size, color)

    @property
    def name(self) -> str:
        return 'Квадрат'

