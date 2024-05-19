# Reverse a String
# Reverse a String using a loop

# input_string = input('Please enter the string to reverse: ')
# reverse_list = list(input_string)
# reverse_list.reverse()
# print(''.join(reverse_list))

while True:
    input_string = input('Please enter the string to reverse: ').strip()
    if input_string != '':
        break
    else:
        print('Invalid value: Please enter a valid string')
        
reverse_string = ''
for char in input_string:
    reverse_string = char + reverse_string
print(f'reverse string is: {reverse_string}')