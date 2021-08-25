# - A set is an unordered collection of items (Has no index).
# - The set itself is mutable. We can add or remove items from it.
# - Every element is unique (no duplicates), can be different types (integer, float, tuple, string) and must be
#   immutable (which cannot be changed so cannot have list, dictionary or another set).
# - Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

# A set is created by placing all the items (elements) inside curly braces {}, separated by comma (unlike dictioaries
# that has key value pairs) or by using the built-in function set().

my_set = {1, 2, 3}
print(my_set)
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set do not have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)  # {1, 2, 3, 4}

# set cannot have mutable items
# my_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'
# here [3, 4] is a mutable list

# we can make set from a list
my_set = set([1,2,3,2])
print(my_set)  # {1, 2, 3}

# Creating an empty set is a bit tricky.
# Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements we use the set()
# function without any argument.
# initialize a with {}
a = {}
print(type(a))  # <class 'dict'>
# initialize a with set()
a = set()
print(type(a))  # <class 'set'>

# Sets dont have indexing
# my_set[0]  # # TypeError: 'set' object does not support indexing