# Leap Year Checker
# Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400)

while True:
    try:
        year = int(input('Please enter a year: '))
        break
    except ValueError as e:
        print('Invalid input : please enter a number')
    except BaseException:
        print('Unexpected error')        

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = 'a leap year'
else:
    result = 'not a leap year'

print(f'{year} is {result}')