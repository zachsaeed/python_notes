# sorted(iterable [, key, reverse = False])
#
# Sorted is different to how sort works.
# sort is an iterable class method and sorts the original iterable whereas
# sorted is a python function that works on anything that is iterable and
# returns a copy of the iterable as a LIST in sorted form

more_nums = [6, 1, 8, 2]
print(sorted(more_nums))  # [1, 2, 6, 8]  # returns a sorted copy of the original
print(more_nums)  # [6, 1, 8, 2]

more_nums.sort()  # works on original
print(more_nums)  # [1, 2, 6, 8]


name = 'Syed  Saquib Saeed'
print(sorted(name))  # [' ', ' ', 'S', 'S', 'S', 'a', 'a', 'b', 'd', 'd', 'e', 'e', 'e', 'i', 'q', 'u', 'y']
print(name)  # Syed Saquib Saeed
# name.sort()  # AttributeError: 'str' object has no attribute 'sort'

# It works it the same way for tuples and sets BUT returns a list
# tuple:
sample_tuple = (1, 3, 2, 4, 8, 5, 7, 6)
print(sorted(sample_tuple))  # [1, 2, 3, 4, 5, 6, 7, 8]

# set:
sample_set = {7, 4, 1, 7, 3, 6,  2, 4, }  # Note: sets cant have copies
print(sorted(sample_set))  # [1, 2, 3, 4, 6, 7]


# We can change the direction by changing the value of 2nd parameter called reverse
# Default is reverse = False which means ascending order

# reverse - True means descending order
nums = [4, 6, 1, 30, 55, 23]
print(sorted(nums, reverse=True))  # [55, 30, 23, 6, 4, 1]

# dictionary
users = [
    {'username': 'saquib', 'tweets': ['I love cake', 'I love pie', 'Hello world']},
    {'username': 'shaheen', 'tweets': ['i Love my cat']},
    {'username': 'nimra', 'tweets': []},
    {'username': 'atif', 'tweets': []},
    {'username': 'faraz', 'tweets': ['Im hungry']},
    {'username': 'rida', 'tweets': []},
]
# A list of dictionaries is a bit tricky to sort as we can't use <, > b/w dictionaries
# If we do we get the following error as there is no way of quantifying dictionaries

# print(sorted(users))  # TypeError: '<' not supported between instances of 'dict' and 'dict'

# To resolve this, we use an optional second parameter called key to specify what/how it
# should be sorted. Key should be equal to a function that accepts a single parameter (single
# item of the iterator) and returns a value which is then used within sort instead of the original value.

# sorts by length of each dictionary (quantity of key/value pairs). In our case,
# each item(dictionary) has the same len = 2
print(sorted(users, key=len))

# sort wrt username
print(sorted(users, key=lambda user: user['username']))

# sort wrt no of tweets
print(sorted(users, key=lambda user: len(user['tweets'])))

# sort wrt no of tweets in descending order
print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))


