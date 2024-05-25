# Generator Function with yield
# Write a generator function that yields even numbers up to a specified limit

specified_limit = 10

def generate_even_numbers(limit):
    for i in range(2,limit+1,2):
        yield i

for num in generate_even_numbers(specified_limit):
    print(num)