from .geomFig import GeomFig, Color


class Rectangle(GeomFig):
    def __init__(self, width: float, height: float, color: Color):
        self._width = width
        self._height = height
        GeomFig.__init__(self, color)

    def area(self) -> float:
        return self._width * self._height

    @property
    def name(self) -> str:
        return 'Прямоугольник'

    def get_data(self) -> str:
        return 'S = {}'.format(self.area())

