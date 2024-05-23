# Function Returning Multiple Values
# Create a function that returns both the area and cicumference of a circle given its radius

import math

while True:
    input_radius = input('Please enter the radius: ')
    if input_radius.isdigit():
        radius = int(input_radius)
        break
    else:
        print('Invalid input: please enter radius value as a number')

def calculate_circle_stats(radius):
    area = round ((math.pi * (radius**2)),2)
    circumference = round((2 * math.pi * radius),2)
    return area,circumference

# tuple unpacking
area,circumference = calculate_circle_stats(radius)
print(f'are of cirlce is {area}')
print(f'circumference of circle is {circumference}')