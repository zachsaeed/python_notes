# all( iterable / generator )
# Returns True if all elements of the iterable are truthy (or if the
# iterable is empty)

# all usually takes a list comprehension as an attribute as the list comprehension
# returns an iterable and is usually used to check weather each tem
# follows a certain rule.

# simplest form:
print(all([0, 1, 2, 3]))  # False because 1,2,3 are all truthy but 0 is falsy
print(all([]))  # True because iterable is empty

# Using list comprehensions (They dont really do anything practically)
# print([char for char in 'eio' if char in 'aeiou']) # ['e', 'i', 'o']
# True as ['e', 'i', 'o'] is truthy
print(all([char for char in 'eio' if char in 'aeiou']))

# print([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # [4, 2, 10, 6, 8]
# True as [4, 2, 10, 6, 8] is truthy
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

# Practical Use example:
# To check each person starts with a C
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
# True because every element passed in is true
print(all([person[0] == 'C' for person in people]))
# print([person[0]=='C' for person in people])  # returns [True, True,
# True, True, True]

people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina', 'Klein']
# False because the last element is False
print(all([person[0] == 'C' for person in people]))
# print([person[0]=='C' for person in people])  # returns [True, True,
# True, True, True, False]

# To check all nums are even
nums = [2, 60, 26, 18]
print(all([num % 2 == 0 for num in nums]))  # True
# print([num % 2 == 0 for num in nums])  # [True, True, True, True]


# any( iterable / generator )
# Returns True if any elements of the iterable are truthy or False if the
# iterable is empty

print(any([0, 1, 2, 3]))  # True

print(any([val for val in [1, 2, 3] if val > 2]))  # True
# print([val for val in [1, 2, 3] if val > 2])  # [3]

print(any([val for val in [1, 2, 3] if val > 5]))  # False
# print([val for val in [1, 2, 3] if val > 5])  # []


# Note: You dont have to pass list comprehension with brackets [] to all and any.
# You can also use generator expressions (List comprehension without brackets) which
# return a generator object
# Example:
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina', 'Klein']
# Here we pass a list comprehension:
print([person[0] == 'C' for person in people])  # [True, True, True, True, True, False]
print(all([person[0] == 'C' for person in people]))  # False
# Here we pass a generator object:
print(person[0] == 'C' for person in people)  # <generator object <genexpr> at 0x00936F70>
print(all(person[0] == 'C' for person in people))  # False


# It is recommended we pass generator expression to all() and any(). It is a lighter weigh
# version of a list, It is'nt a list but can be used to generate one. It is an intermediate
# and can be used in tasks where we dont need a list in the end. So using generator expressions
# is more lighter weight by saving memory and making things less intensive.
# or more info see:
# https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension

