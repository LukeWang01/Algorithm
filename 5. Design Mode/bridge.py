# class Shape:
#     pass
#
#
# class Line(Shape):
#     pass
#
# class Rectangle(Shape):
#     pass
#
# class Circle(Shape):
#     pass
#
# class RedLine(Line):
#     pass
#

from abc import ABCMeta, abstractclassmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractclassmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractclassmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    
    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    def draw(self):
        self.color.paint(self)


