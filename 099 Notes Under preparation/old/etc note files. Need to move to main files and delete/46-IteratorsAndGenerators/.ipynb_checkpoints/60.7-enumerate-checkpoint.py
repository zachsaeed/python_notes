# A lot of times when dealing with iterators, we also get a need to keep a count of
# iterations. Python eases the programmers’ task by providing a built-in function
# enumerate() for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate
# object. This enumerate object can then be used directly in for loops or be converted
# into a list(), tuple(), set() and many more.

# enumerate(iterable, start=0)
#   Iterable: any object that supports iteration
#   Start: the index value from which the counter is to be started, by default it is 0

# Python program to illustrate enumerate function
programmming = ["Python", "Programmming", "Is", "Fun"]
print(type(programmming))

enum = enumerate(programmming)
print(type(enum))

# Note: Once list(), tuple(), set() is called on enum, it cannot be accessed again

# Converting to a list of tuples
print(list(enum))  # [(0, 'Python'), (1, 'Programmming'), (2, 'Is'), (3, 'Fun')]

# Comment out previous conversions on enum or else this will print empty tuple.
# Converting to a tuple  of tuples
# print(tuple(enum))  # ((0, 'Python'), (1, 'Programmming'), (2, 'Is'), (3, 'Fun'))

# Comment out previous conversions on enum or else this will print empty set.
# Converting to a set  of tuples
# print(set(enum))  # {(0, 'Python'), (3, 'Fun'), (1, 'Programmming'), (2, 'Is')}


# for loop
programmming = ["Python", "Programmming", "Is", "Fun"]
# printing the tuples in object directly
for item in enumerate(programmming):
    print(item)
# (0, 'Python')
# (1, 'Programmming')
# (2, 'Is')
# (3, 'Fun')


# changing index and printing separately
for count, item in enumerate(programmming,100):
    print(count, item)
# 100 Python
# 101 Programmming
# 102 Is
# 103 Fun
