# Validate Input
# Keep asking the user for input until they enter a number between 1 and 10

while True:
    input_number = input('Enter number b/w 1 and 10: ')
    if input_number.isdigit():
        number = int(input_number)
        if number>=1 and number<=10:
            break
        else:
            print('Invalid input: please enter number between 1 and 10')
    else:
        print('Invalid input: please enter a number')
print(f'The number which you are entered is {number}')