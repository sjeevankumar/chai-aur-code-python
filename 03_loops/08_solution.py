# Prime Number Checker
# Check if a number is prime

while True:
    input_number = input('Please enter a number: ')
    if input_number.isdigit():
        number = int(input_number)
        break
    else:
        print('Invalid input: Please enter a valid number')

is_prime = True
for i in range(2,number):
    if (number%i) == 0:
        is_prime = False
        break
if is_prime:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
