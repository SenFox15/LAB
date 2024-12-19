#Задание 1
import math

def calculate_area(shape, *args):
   
    if shape.lower() == 'circle':
        if len(args) != 1 or args[0] <= 0:
            print("Error: Circle needs one positive radius.")
            return None
        radius = args[0]
        return math.pi * radius**2
    elif shape.lower() == 'rectangle':
        if len(args) != 2 or args[0] <= 0 or args[1] <= 0:
            print("Error: Rectangle needs two positive dimensions.")
            return None
        length, width = args
        return length * width
    elif shape.lower() == 'triangle':
        if len(args) != 2 or args[0] <= 0 or args[1] <= 0:
            print("Error: Triangle needs a positive base and height.")
            return None
        base, height = args
        return 0.5 * base * height
    elif shape.lower() == 'square':
        if len(args) != 1 or args[0] <= 0:
            print("Error: Square needs one positive side length.")
            return None
        side = args[0]
        return side**2
    else:
        print("Error: Unknown shape.")
        return None


circle_area = calculate_area('circle', 5)
rectangle_area = calculate_area('rectangle', 4, 6)
triangle_area = calculate_area('triangle', 3, 8)
square_area = calculate_area('square', 7)

print(f"Area of circle: {circle_area}")
print(f"Area of rectangle: {rectangle_area}")
print(f"Area of triangle: {triangle_area}")
print(f"Area of square: {square_area}")

invalid_area = calculate_area('rectangle', -2,5) 

#Задание 2

def count_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10) 

num_digits = count_digits(12345)
print(f"The number of digits in 12345 is: {num_digits}")


