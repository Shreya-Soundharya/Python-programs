#Program to find area using functions

import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def calculate_square_area(side):
    return side**2

def calculate_square_perimeter(side):
    return 4 * side

choice = input("Enter the shape (circle, rectangle, triangle, square): ").lower()

if choice == 'circle':
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    perimeter = calculate_circle_perimeter(radius)
elif choice == 'rectangle':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)
elif choice == 'triangle':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculate_triangle_area(base, height)
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
elif choice == 'square':
    side = float(input("Enter the length of the square's side: "))
    area = calculate_square_area(side)
    perimeter = calculate_square_perimeter(side)
else:
    print("Invalid shape entered.")
    area = 0
    perimeter = 0

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
