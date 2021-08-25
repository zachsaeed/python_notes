# First class functions
# https://www.google.com/search?q=python+functions+are+objects&rlz=1C5CHFA_enPK743PK743&oq=python+functions+are+objects&aqs=chrome..69i57j0l3j69i64.5473j0j4&sourceid=chrome&ie=UTF-8
# A programming language is said to have First-class functions when functions in that
# language are treated like any other variable. For example, in such a language, a
# function can be passed as an argument to other functions, can be returned by another
# function and can be assigned as a value to a variable.

# Higher-order functions:
# Higher-order functions are functions that work on other functions, meaning that they
# take one or more functions as an argument and can also return a function.
# eg Map, Filter

# Callback function:
# In a higher order function, when one of the parameters passed in is a function, that
# function is a callback function because it will be called back and used within the
# higher order function.

# Accepting function as arguments
def sum(n, func):
    total = 0
    for num in range(1, n + 1):
        total += func(num)
    return total


def square(x):
    return x * x


def cube(x):
    return x * x * x


print(sum(3, cube))
print(sum(3, square))  # 5


# Returning a function
# We can return funcs from other funcs
from random import choice


def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh


laugh = make_laugh_func()
print(laugh())
