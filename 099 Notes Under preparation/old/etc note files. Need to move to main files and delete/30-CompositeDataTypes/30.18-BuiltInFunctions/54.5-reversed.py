# reversed(iterable [, key, reverse = False])
#
# reversed is different to how reverse works.
# reverse is an iterable class method and reverses the original iterable whereas
# reversed is a python function that works on anything that is iterable (like string,
# range etc) and returns a copy of the iterable as a list_reverseiterator object
# in reversed form which can be converted into a list

more_nums = [6, 1, 8, 2]
print(reversed(more_nums))  # <list_reverseiterator object at 0x0326FD50>
print(list(reversed(more_nums)))  # [2, 8, 1, 6]  # convert to list using list() method
print(more_nums)  # [6, 1, 8, 2] # original iterator stays the same

more_nums.reverse()  # updates original
print(more_nums)  # [2, 8, 1, 6]

# String
string_var = 'hello world!'
# we can get a reverse string like this:
reversed_string_var = reversed(string_var)
print(reversed_string_var)  # <reversed object at 0x01B5BEB0>
list_reversed_string_var = list(reversed_string_var)
print(list_reversed_string_var)  # ['!', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
new_string_var = ''.join(list_reversed_string_var)  # !dlrow olleh

# NOTE: shorter way we can also reverse via slicing
print(string_var[::-1])  # !dlrow olleh

# we can run a for loop through the reversed object
for char in reversed(string_var):
    print(char)

# range()
reversed_iter_obj = reversed(range(0, 10))
print(reversed_iter_obj)  # <range_iterator object at 0x02CEA230>
print(list(reversed_iter_obj))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# TODO have a look at sequence protocol
# https://stackoverflow.com/questions/43566044/what-is-pythons-sequence-protocol
# https://www.programiz.com/python-programming/methods/built-in/reversed
# Also, reveresed returns diferent objects for different iterators. have a look at that


# TODO have a look at diff between (vid: 197)
# sequence (string, tuple, list, range)
# collection (dictionary, set)
# https://www.quora.com/What-are-sequences-and-what-are-collections-in-Python-Where-does-list-tuple-string-dictionary-set-etc-fit-in
# https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6