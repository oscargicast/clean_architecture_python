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

    def area(self) -> float:
        """This area in in m2"""
        return self.length**2


def area_in_cm_2(shape: Shape):
    return shape.area() * 10000


if __name__ == "__main__":
    circle = Circle(10)
    area_cm2_circle = area_in_cm_2(shape=circle)
    print(f"{area_cm2_circle = :.2f}")

    rectangle = Rectangle(10, 20)
    area_cm2_rectangle = area_in_cm_2(shape=rectangle)
    print(f"{area_cm2_rectangle = :.2f}")

    square = Square(10)
    area_cm2_square = area_in_cm_2(shape=square)
    print(f"{area_cm2_square = :.2f}")
