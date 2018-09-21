class Color:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    def __str__(self) -> str:
        return self._color



