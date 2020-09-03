# https://repl.it/repls/ShrillDarkcyanVirtualmachine#main.py
import math


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, squareOrRectangle):
        area = self.get_area()
        otherArea = squareOrRectangle.get_area()
        return math.trunc(area / otherArea)

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side: int):
        self.width = side
        self.height = side
        self.side = side

    def set_side(self, side: int):
        self.width = side
        self.height = side
        self.side = side

    def __repr__(self):
        return f'Square(side={self.side})'

    def set_width(self, width: int):
        self.set_side(width)

    def set_height(self, height: int):
        self.set_side(height)
