# Recursive Function
# Create a recursive function to calculate the factorial of a number

while True:
    input_number = input('Please enter the number: ')
    if input_number.isdigit():
        number = int(input_number)
        break
    else:
        print('Invalid input: please enter the valid number')

def recursive_factorial(num):
    if num == 0:
        return 1
    return num * recursive_factorial(num-1)

print(recursive_factorial(number))

    