# Default Parameter Value
# Write a function that greets a user. If no name is provided, it should greet with a default name.

input_name = input('Please enter the name: ').strip()

def greet_user(name='guest user'):
    print(f'welcome {name}') if name else print('welcome guest user')
        
greet_user(input_name)