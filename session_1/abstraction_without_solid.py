import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        """This area in in m2"""
        return math.pi * self.radio**2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """This area in in m2"""
        return self.width * self.height


class Square(Shape):
    def __init__(self, length: float):
        self.length = length

    def area_m2(self) -> float:
        """This area in in m2"""
        return self.length**2


def area_in_cm_2(
    width: float | None = None,
    height: float | None = None,
    radio: float | None = None,
):
    if width is not None and height is not None:
        if width == height:
            shape = Square(width)
        elif width != height:
            shape = Rectangle(width, height)
    if radio:
        shape = Circle(radio)
    # Duck typing, nada nos asegura que todas las
    # instancias tengan el método area.
    return shape.area() * 10000


if __name__ == "__main__":
    area_cm2_circle = area_in_cm_2(radio=10)
    print(f"{area_cm2_circle = :.2f}")

    area_cm2_rectangle = area_in_cm_2(width=10, height=20)
    print(f"{area_cm2_rectangle = :.2f}")

    # area_cm2_square = area_in_cm_2(width=10, height=10)
    # print(f"{area_cm2_square = :.2f}")
