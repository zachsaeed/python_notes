from functools import wraps
# wraps preserves a functions metadata when it is decorated
# It is a wrapper function we use to wrap our wrapper function


def log_function_data(fn):
    @wraps(fn)  # decorator to replace ou wrapper's metadata with fn's
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y


print(add.__doc__)  # Adds two numbers together.
print(add.__name__)  # add
help(add)  # Help on function add in module __main__:
#            add(x, y)
#                Adds two numbers together.

