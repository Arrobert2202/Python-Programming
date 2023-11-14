import math

class Shape():
  name = "Shape"
  
  def perimeter(self):
    return None
  
  def area(self):
    return None
  
class Circle(Shape):
  name = "Circle"

  def __init__(self, radius):
    self.radius = radius
  
  def perimeter(self):
    return 2 * math.pi * self.radius
  
  def area(self):
    return math.pi * self.radius ** 2


class Rectangle(Shape):
  name = "Rectangle"

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def perimeter(self):
    return 2 * self.length + 2 * self.width
  
  def area(self):
    return  self.length * self.width
  
class Triangle(Shape):
  name = "Triangle"

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def perimeter(self):
    return self.a + self.b + self.c
  
  def area(self):
    semiperimeter = self.perimeter() / 2
    return math.sqrt(semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c))

circle = Circle(4)

print(f"Shape: {circle.name}")
print(f"Perimeter: {circle.perimeter()}")
print(f"Area: {circle.area()}")
print()

rectangle = Rectangle(5, 8)

print(f"Shape: {rectangle.name}")
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Area: {rectangle.area()}")
print()

triangle = Triangle(5, 3, 4)

print(f"Shape: {triangle.name}")
print(f"Perimeter: {triangle.perimeter()}")
print(f"Area: {triangle.area()}")
print()