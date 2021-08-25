# You can provide a documentation for your own objects (functions for example)
# in the body of their definition as a string surrounded by three double-quotes:
#  """message"""
# has to be the first line inside function or class body
# can be accessed using the __doc__ property of the function


def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"


print(say_hello.__doc__)  # A simple function that returns the string hello

# Similarly, built-in functions have the same __doc__ property
print(print.__doc__)
print(len.__doc__)
print([1, 2, 3].pop.__doc__)


# Similarly classes:
class User:
    """A simple class"""
    pass  # use pass as empty classes not allowed and throw errors

user1 = User()
print(user1.__doc__)  # A simple class

