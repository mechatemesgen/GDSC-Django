import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.calculate_area()}")
