# - Generators are a type of (Subset of) iterators.
#   ie. All generators are iterators but all iterators are no generator
# - Generators can be created in one of two ways
# 1- with generator functions which use the yield keyword
# 2- with generator expressions

# Generator Functions: Is a way of creating a generator (which is an iterator)
# - Normal functions use 'return'
#   returns once
#   When invoked, returns the return value

# - whereas, a Generator functions uses 'yield' to return
#   can yield multiple times
#   When invoked, returns a generator


# Example A generator function which creates a generator:
def count_up_to(max):
    count = 1
    while count <= max:
        # below will return the value of count and pause and stay that way
        # until next is called on count_up_to
        yield count
        count += 1


my_generator = count_up_to(5)
print(my_generator)  # <generator object count_up_to at 0x015C6D70>

print(next(my_generator))  # 1
print(next(my_generator))  # 2
print(next(my_generator))  # 3
print(next(my_generator))  # 4
print(next(my_generator))  # 5

# Since yield returns and pauses, each next keeps track of the current value
# and returns the next value when next is called again. This happens until
# the StopIteration error is thrown. If we call it again:
# print(next(my_generator))  # StopIteration Error

# For example, when next is called on a generator and then it is passed in a for loop,
# the loop starts from the last time when next was called
my_generator2 = count_up_to(5)
print(next(my_generator2))  # 1
for num in my_generator2:
    print(num)
# 2
# 3
# 4
# 5

# Note: Creating an iterable/iterator involves creating a class with __iter__ () and
# __next__() and is a longer way of doing things compared to a generator which is
# created by a function that calls yield. It has __iter__ ad __next__ already setup:
help(my_generator)
# Generator is a way of making an iterator quickly. Takes up less memory and is faster
# Unlike an iterable (like list or string) that holds all the items at once, generator
# generates one value at a time thus saving lots of memory. Like range()

