# filter( function, iterable )
# - A standard function that accepts at least 2 arguments, a function (named or lambda)
#   "with one parameter" and an iterable (string, list, dictionary, set, tuple)
# - It returns a map object which contains only the items for which the lambda returns true thus,
#   "filtering" away those that are false.
# - The map object can be converted to another data structure
# - We dont have to use lambda and can use normal function name

# Using filter to get evens
num = [1, 2, 3, 4, 5, 6, 7]
evens = filter(lambda item: item % 2 == 0, num)
print(evens)  # <filter object at 0x030D0E90>
print(list(evens))  # [2, 4, 6]


# @TODO we can use list comprehension to do the above. Verify this