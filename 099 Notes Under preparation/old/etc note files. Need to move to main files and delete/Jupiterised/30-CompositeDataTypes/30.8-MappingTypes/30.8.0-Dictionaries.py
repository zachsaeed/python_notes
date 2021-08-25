# Dictionary
# a data structure that stores key:value pairs
# We use the 'keys' to describe our data (as labels) and the 'values' to represent that data
# INTERVIEW
# Unlike a list, a dictionary is not a sequence ie no indexes or slicing
# Note: Python 3.7: Dictionaries preserve insertion order. Updating a key does not affect the order. Keys added after
# deletion are inserted at the end.
# Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering). Order
# comparisons (‘<’, ‘<=’, ‘>=’, ‘>’) raise TypeError.

# Creating Dictionaries:
# 1- Using curly braces
my_dictionary = {
    'name': 'Saquib',
    44: 'my favourite number',
    'address': 'chadwell heath',
    'pet': 'cat'
} # key and values are separated by a colon. Each element is separated by comma

# 2- Using the dict function
my_dictionary2 = dict(name='Saquib', address='chadwell heath', pet='cat')
print(my_dictionary2)
# Note: with dict we cannot define integers as keys eg 4='my favourite number' is syntactically incorrect and you get:
# SyntaxError: keyword can't be an expression.

# To avoid this issue we can pass a predefined dictionary to dict
my_dictionary_3 = dict({'name': 'Saquib', 44: 'my favourite number', 'address': 'chadwell heath', 'pet': 'cat'})
print(my_dictionary_3)


# To access the dictionary items, we use keys
print(my_dictionary['name'])  # Saquib
# print(my_dictionary['surname'])  # does no exist KeyError: 'surname'

# We can also use a var (with the key as value)
my_key_var  = 44
print(my_dictionary[my_key_var])  # 'my favourite number'