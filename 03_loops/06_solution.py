# Factorial Calculator
# Compute the factorial of a number using a while loop

while True:
    input_number = input('Please enter the number: ')
    if input_number.isdigit():
        number = int(input_number)
        break
    else:
        print('Invalid input: Please enter the number')
        
i=2
factorial = 1
while i<=number:
    factorial*=i
    i+=1
print(f'Factorial of {number} is: {factorial}')



# i = number
# factorial = 1
# while i>1:
#     factorial*=i
#     i-=1
# print(factorial)

