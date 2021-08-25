# Iterables and Iterators
# all()	Returns True if all elements of an iterable are true
# any()	Returns True if any elements of an iterable are true
# enumerate()	Returns a list of tuples containing indices and values from an iterable
# filter()	Filters elements from an iterable
# iter()	Returns an iterator object
# len()	Returns the length of an object
# map()	Applies a function to every item of an iterable
# next()	Retrieves the next item from an iterator
# range()	Generates a range of integer values
# reversed()	Returns a reverse iterator
# slice()	Returns a slice object
# sorted()	Returns a sorted list from an iterable
# zip()	Creates an iterator that aggregates elements from iterables

# https://pynative.com/python-range-function/

# range() function is usually used within for loops and returns a range object
# Syntax:
# range ([start,] stop [, step]) #start (default 0) and step (default 1) are optional
print("Printing All odd numbers between 1 and 10 using range()")
for i in range(1, 10, 2):
    print(i, end=', ')

#Note:
# - range() function only works with the integers i.e., whole numbers. Therefore,
#   all argument must be integers. You can not pass a string or float number or
#   any other type in a start, stop and step argument of a range().
# - All three arguments can be positive or negative.
# - The step represents the difference in the sequence of numbers so, value must not be zero.
#   If a step is zero python raises a ValueError exception.
# - The range(n) is of exclusive nature that is why it doesn’t include the last number in the
#   output i.e. The given endpoint is never part of the generated result.
#   For example, range(0, 5) = [0,1,2,3,4]
# - Python 3’s range uses the generator. Python 3’s range() will produce value when for loop
#   iteration asked for it. i.e., it  The range() doesn’t produce all numbers at once.
#   Therefore following example will not work:
print('\nPrinting range method:')
print(range(0,5))
# - Python range() function returns an immutable sequence object of integers, so its possible
#   to convert range() output to python list. Use list class to convert range output to list.
#   For example:
print("\nConverting python range() to list")
even_list = list( range(2,10,2))
print("printing list", even_list)


# Access Python range() result with its index value
# - range() is constructor returns a range object which is nothing but a sequence of numbers,
#   this range object can also be accessed by its index using slice notation. It supports both
#   positive and negative indices.
print("\naccessing python range objet with its index")
first_number = range(0,10)[0] # Printing 0th position number i.e. index ZERO means first number
print("\nFirst number in given range is:  ", first_number)
fifth_number = range(0,10)[4]
print("\nfifth number in given range is:  ", fifth_number)


# reverse() function
# To get sequence of numbers in descending order, there are 2 ways of doing this:
# First i to use -ve step value
print("\nDisplaying list of numbers by reverse order using range()")
for number in range(4,-1,-1):
    print (number, end=', ')
#Alternatively, use the reversed function.
print("\nDisplaying list of numbers by reverse order using range()")
for i in reversed(range(5)):
    print(i, end=', ')


# chain() function
# we can concatenate the output of two range functions using chain() function of
# itertools library
from itertools import chain
print("\nConcatenated two range() function")
concatenated_range = chain(range(10), range(50, 75))
for num in concatenated_range:
    print(num,end=", ")


# range() function works differently between Python 3 and Python 2.
# The difference between range() and xrange() functions becomes relevant only when you are using python 2.

# Working of range and xrange in Python 2
# - Both the range() and xrange() function generates the sequence of numbers. But range()produce a list, and
#   xrange()produces an xrange object i.e. a sequence object of type xrange.
# - range() generates all numbers at once.
# - xrange() doesn’t generate all numbers at once. it produces number one by one as for loop moves to
#   the next number
# In Python 3, xrange() is renamed to range() and original range() function was deprecated.