# Basic Function Syntax
# Write a function to calculate and return the square of a number

while True:
    input_number = input('Please enter the number: ')
    if input_number.isdigit():
        number = int(input_number)
        break
    else:
        print('Invalid input: Please enter valid number')

def calculate_square(num):
    return num**2

result = calculate_square(number)
print(f'square of {number} is {result}')