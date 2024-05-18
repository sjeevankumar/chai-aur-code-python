# Multiplication Table Printer
# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

while True:
    given_number = input('Please enter the number: ')
    if given_number.isdigit():
        number = int(given_number)
        break
    else:
        print('Invalid input: Please enter a number')
        
for i in range(1,11):
    if i == 5:
        continue
    result = number*i
    print(f'{number} * {i} = {result}')