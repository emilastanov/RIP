from abc import ABC, abstractmethod
from .color import Color


class GeomFig(ABC):
    def __init__(self, color: Color):
        self._color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def get_data(self) -> str:
        pass

    def __str__(self) -> str:
        return '{} {} ({})'.format(self._color, self.name, self.get_data())

