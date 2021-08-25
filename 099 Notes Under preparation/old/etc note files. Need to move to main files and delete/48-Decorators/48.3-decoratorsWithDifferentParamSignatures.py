# In the last example, the decorated functions, greet and rage didnt accept any
# arguments. We need our decorator to work with any number of arguments which is
# the standard decorator pattern

# To do this, we make our wrapper function (which is decorator returned) accept unlimited
# number of arguments and keyword arguments (*args and **kwargs)

# Syntax:

# This version works with any number of args


def shout(fn):
    def wrapper(*args, **kwargs):
        """I am the wrapper"""
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    """I am greet"""
    return f"Hi, I'm {name}."


@shout
def order(main, side):
    """I am order"""
    return f"Hi, I'd like the {main}, with a side of {side}, please."


@shout
def lol():
    return "lol"


print(greet("todd"))  # HI, I'M TODD.
# HI, I'D LIKE THE FRIES, WITH A SIDE OF BURGER, PLEASE.
print(order(side="burger", main="fries"))
print(lol())  # LOL


# What actually happening is:
def shout_decorator(fn):
    def wrapper(*args, **kwargs):
        upper = fn(*args, **kwargs).upper()
        return upper
    return wrapper


def greet1(name):
    return f"Hi, I'm {name}."


def order1(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


def lol1():
    return "lol"


# Here we return the wrapper (Decorated function):
greet_decorated = shout_decorator(greet1)
order_decorated = shout_decorator(order1)
lol_decorated = shout_decorator(lol1)

print(greet_decorated("todd"))  # HI, I'M TODD.
print(order_decorated(side="burger", main="fries"))  # HI, I'D LIKE THE FRIES, WITH A SIDE OF BURGER, PLEASE.
print(lol_decorated())  # LOL


# There is a problem when using decorators. When we try to access the meta data (__doc__,
# __name__ and help()) on he decorated functions, it return meta for the wrapper function
# as it is actually he wrapper function that is being called
print(greet.__doc__)  # I am the wrapper
print(greet.__name__)  # wrapper
help(greet)  # Help on function wrapper in module __main__:
#              wrapper(*args, **kwargs)
#                  I am the wrapper
# To return the original metadata, we use the wrap library as shown in the next topic
