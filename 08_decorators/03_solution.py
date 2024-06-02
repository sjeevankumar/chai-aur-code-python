# Catch Return Values
# Implement a decorator that catches the return values of a function, so that when it is called with the same arguments, the cached value is returned instead of re-executing the function

import time

def cache(func):
    cache_value = {}
    def wrapper(*args,**kwargs):        
        if args in cache_value:
            return cache_value[args]
        result = func(*args,**kwargs)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))

