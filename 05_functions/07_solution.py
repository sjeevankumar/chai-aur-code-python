# Function with *args
# Write a function that takes variable number of arguments and returns their sum

def calculate_sum(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

result = calculate_sum(1,2,3,4)
print(f'sum is {result}')