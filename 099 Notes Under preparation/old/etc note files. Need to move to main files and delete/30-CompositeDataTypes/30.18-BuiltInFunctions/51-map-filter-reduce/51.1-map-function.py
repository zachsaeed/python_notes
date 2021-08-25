# These are higher order functions.
# Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer
# to write simpler, shorter code, without necessarily needing to bother about intricacies
# like loops and branching.

# Essentially, these three functions allow you to apply a function across a number of iterables,
# in one full swoop. map and filter come built-in with Python (in the __builtins__ module) and
# require no importing. reduce, however, needs to be imported as it resides in the functools
# module.


# map( function, iterable )
# - Accepts at least 2 arguments, a function (named or lambda) which takes one parameter and an
#   iterable (string, list, dictionary, set, tuple)
# - It runs the lambda function on each iterable and returns a map object which can
#   be converted to another data structure

# Using lambda function
num = [2, 4, 6, 10]
doubles = map(lambda item: item*2, num)
print(doubles)  # <map object at 0x030D0E90>
print(list(doubles))  # [4, 8, 12, 20]

# We dont have to use lambda and can use normal unction
def doubleFunction(x):
    return x*2
doubles2 = map(doubleFunction, num)
print(doubles2)  # <map object at 0x030D0E90>
print(list(doubles2))  # [4, 8, 12, 20]


# Because of map(), we dont need a for loop to run through each item of an iterable

# more examples
# create a list of first names only
names=[
    {'first': 'Saquib', 'last': 'Saeed'},
    {'first': 'Rida', 'last': 'Saquib'},
    {'first': 'John', 'last': 'Doe'}
]

firstNamesMap = map(lambda x: x['first'], names)
print(list(firstNamesMap))  # ['Saquib', 'Rida', 'John']


# @TODO we can use list comprehension to do the above. Verify this