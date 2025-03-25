from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def area(self):
        return self._length * self._width

    @property
    def perimeter(self):
        return 2 * (self._length + self._width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self.length  # Since length == width in a square


class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self._major_radius = major_radius
        self._minor_radius = minor_radius

    @property
    def major_radius(self):
        return self._major_radius

    @property
    def minor_radius(self):
        return self._minor_radius

    @property
    def area(self):
        return pi * self._major_radius * self._minor_radius

    @property
    def perimeter(self):
        raise NotImplementedError("The perimeter of an ellipse cannot be computed with a simple formula.")


class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)

    @property
    def radius(self):
        return self.major_radius  # Since major_radius == minor_radius in a circle

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius
