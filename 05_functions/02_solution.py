# Function with Multiple Parameters
# Create a function that takes two numbers as parameters and returns their sum

while True:
    input_number1 = input('Please enter the first number: ')
    if input_number1.isdigit():
        number1 = int(input_number1)
        break
    else:
        print('Invalid input: Please enter the valid number')

while True:
    input_number2 = input('Please enter the second number: ')
    if input_number2.isdigit():
        number2 = int(input_number2)
        break
    else:
        print('Invalid input: Please enter the valid number')

def calculate_sum(num1,num2):
    return num1+num2

result = calculate_sum(number1,number2)
print(f'sum of {number1} and {number2} is {result}')