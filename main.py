#Geometric Shape Calculator

import math

class Shape:
    def __init__(self, units="centimeters"):
        self.units = units
#polymorphism     
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius, units="centimeters"):
        super().__init__(units)
        self.radius = radius
#polymorphism
    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width, units="centimeters"):
        super().__init__(units)
        self.length = length
        self.width = width
#polymorphism
    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3, units="centimeters"):
        super().__init__(units)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

#polymorphism
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

def main():
    while True:
        shape = input("Enter the shape (circle, rectangle, triangle): ").lower()

        if shape == "circle":
            radius = float(input("Enter the radius of the circle in centimeters: "))
            circle = Circle(radius)
            area = circle.calculate_area()
            perimeter = circle.calculate_perimeter()
            print("Area:", area, "square", circle.units)
            print("Circumference:", perimeter, circle.units)
            break
        
        elif shape == "rectangle":
            length = float(input("Enter the length of the rectangle in centimeters: "))
            width = float(input("Enter the width of the rectangle in centimeters: "))
            rectangle = Rectangle(length, width)
            area = rectangle.calculate_area()
            perimeter = rectangle.calculate_perimeter()
            print("Area:", area, "square", rectangle.units)
            print("Perimeter:", perimeter, rectangle.units)
            break
        
        elif shape == "triangle":
            side1 = float(input("Enter the length of side 1 of the triangle in centimeters: "))
            side2 = float(input("Enter the length of side 2 of the triangle in centimeters: "))
            side3 = float(input("Enter the length of side 3 of the triangle in centimeters: "))
            triangle = Triangle(side1, side2, side3)
            area = triangle.calculate_area()
            perimeter = triangle.calculate_perimeter()
            print("Area:", area, "square", triangle.units)
            print("Perimeter:", perimeter, triangle.units)
            break
        
        elif shape == "quit":
            break
        
        else:
            print("Invalid shape entered. Please enter 'circle', 'rectangle', or 'triangle'.")
          
            shape = input("Enter the shape (circle, rectangle, triangle): ").lower()


main()