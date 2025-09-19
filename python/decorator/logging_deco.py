from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result of {func.__name__} is {result}")
        return result
    return wrapper

@log_activity
def add(a, b):
    return a + b

add(1, 2)