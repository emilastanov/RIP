from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
from lab_python_oop.color import Color


def main():
    rectangle = Rectangle(3, 2, Color('Голубой'))
    circle = Circle(5, Color('Красный'))
    square = Square(5, Color('Желтый'))

    figures = [rectangle, circle, square]
    result = '\n '.join(str(figure) for figure in figures)

    print("Заданы следующие фигуры:\n", result)


if __name__ == '__main__':
    main()