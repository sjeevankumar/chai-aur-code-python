# Sum of Even Numbers
# Calculate the sum of even numbers up to a given number n.

sum_even = 0

while True:
    n_input = input('enter the value of n: ')
    if n_input.isdigit():
        n = int(n_input)
        break
    else:
        print('Invalid input: Please enter n as a positive integer')
    
for num in range(1,n+1):
    if num % 2 == 0:
        sum_even += num

print(f'Sum of even numbers is {sum_even}')