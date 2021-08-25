# We can pass other arguments (besides fn) to decorators aswell
# Essentially its a multilayer process. We need an extra layer of function because
# of the argument we are trying to pass in.

# Example: The following code ensures that the first argument is something specific
# which we can specify in the decorator

from functools import wraps


def ensure_first_arg_is(val):
    def inner(fn):  # This is the actual decorator
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"Invalid! First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    return foods


print(fav_foods("burrito", "ice cream"))  # ('burrito', 'ice cream')

print(fav_foods("ice cream", "burrito"))  # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2


print(add_to_ten(10, 12))  # 22
print(add_to_ten(1, 2))  # 'Invalid! First argument must be 10'


# We're really doing:
# func = decorator_with_args(arg)(func)
# where decorator_with_args(arg) returns inner
# and then inner(func) is called which returns the wrapper
