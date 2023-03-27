# Calculator to calculate area of a sphere
# Read radius as input from the user

import math

# Circumference: 2 * pi * R
# Area: 4 * pi * R * R

radius = int(input("Please enter radius: \n"))

area = 4 * math.pi * radius * radius
print(f"area of the sphere is: {area}")