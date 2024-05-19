# Find the First Non-Repeated Character
# Given a string, find the first non-repeated character

while True:
    input_string = input('Please enter the string: ').strip()
    if len(input_string) != 0:
        break
    else:
        print('Invalid input: Please enter valid string')    

non_repeated_char = ''

for char in input_string:
    if input_string.count(char) == 1:
        non_repeated_char = char
        break
if len(non_repeated_char) != 0:
    print(f'the first non-repeated character: {non_repeated_char}')
else:
    print('there is no non repeated character in the given string')


     