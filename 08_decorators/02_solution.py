# Debugging function calls
# Create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{k} = {v}' for k,v in kwargs.items())
        print(f'calling: {func.__name__} function with args { args_value if args_value else 0} and kwargs {kwargs_value}')
        return func(*args,**kwargs)
    return wrapper

@debug
def greet(name,greeting = 'Hello'):
    print(f'{greeting}, {name}')
    
greet(name = 'jeevan')