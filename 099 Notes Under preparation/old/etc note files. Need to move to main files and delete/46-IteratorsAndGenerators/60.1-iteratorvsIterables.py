# Iterator - an object that can be iterated upon (we can run a for-loop on). An
# object which returns data, one element at a time when next() is called on it
# until it hits the end.

# Iterable: - An object which will return an iterator when iter() is called on it

# Example "Hello" is an iterable but is not an iterator
# iter("Hello") returns an iterator

my_string = "Hello"  # String is an iterable
# my_string.next()  # AttributeError: 'str' object has no attribute 'next'
my_iterator = iter(my_string)  # get the iterator
print(next(my_iterator))  # H
print(next(my_iterator))  # e
print(next(my_iterator))  # l
print(next(my_iterator))  # l
print(next(my_iterator))  # o
# print(next(my_iterator))  # StopIteration Error


# - When we run a for loop on a string, behind the scenes it takes the string
#   (iterable) calls iter() on it to get the iterator and then keeps on calling
#   next() on the iterator until it raises a StopIterationError which it catches
#   and then stops.
# - This is the standard protocol that needs to be setup in any iterator that
#   exists or that we define

for ch in my_string:
    print(ch)
# H
# e
# l
# l
# o

# Similarly [ist] is an iterable aswell.
