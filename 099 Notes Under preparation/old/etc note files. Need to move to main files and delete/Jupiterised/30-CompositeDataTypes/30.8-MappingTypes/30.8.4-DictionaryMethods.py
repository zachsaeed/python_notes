# Changed in version 3.8: Dictionary views are now reversible as they preserve insertion order.

# clear()
# empty out a dictionary
d = dict(a=1, b=2, c=3)
print(d)  # {'a': 1, 'b': 2, 'c': 3}
d.clear()
print(d)  # {}


# copy()
# Will make a copy (clone) of the dictionary
d = dict(a=1, b=2, c=3)
d2 = d.copy()
print(d == d2)  # True  # same values / structure
print(d is d2)  # false # different references


# fromKeys(key_iterable_collection, value)
# creates key-value pair using the same value for all keys in the iterable collection
# Its usually called on an empty dictionary or dict()
# Used to create default dictionaries to assign initial starting values to properties
# list of keys
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unkown')
print(new_user)  # {'name': 'unkown', 'score': 'unkown', 'email': 'unkown', 'profile bio': 'unkown'}
new_user3 = {}.fromkeys(['name'], 'unkown')
print(new_user3)  # {'name': 'unkown'}
# A string as key  will use each character of the string as key
new_user2 = {}.fromkeys('name', 'unkown')
print(new_user2)  # {'n': 'unkown', 'a': 'unkown', 'm': 'unkown', 'e': 'unkown'}
# range
new_user3 = {}.fromkeys(range(1,10), 'unkown')
print(new_user3)  # {1: 'unkown', 2: 'unkown', 3: 'unkown', 4: 'unkown', 5: 'unkown', 6: 'unkown', 7: 'unkown', 8: 'unkown', 9: 'unkown'}


# get( key )
# Returns the value of a key.
# Returns 'None' if key doesnt exist
my_dictionary = {
    'name': 'Saquib',
    44: 'my favourite number',
    'address': 'chadwell heath',
    'pet': 'cat'
}
print(my_dictionary.get('name'))  # Saquib
# when key doesnt exist, get does not generate an error
# print(my_dictionary['surname'])  # KeyError: 'surname'
print(my_dictionary.get('surname'))  # None


# pop( key_value )
# pop() expects at least 1 argument
print(my_dictionary.pop('name'))
# print(my_dictionary.pop())  # TypeError: pop expected at least 1 arguments, got 0
# print(my_dictionary.pop('surname'))  # TypeError: pop expected at least 1 arguments, got 0  KeyError: 'surname'


# popitem()
# Removes a random key in a dictionary. It takes no arguments
print(my_dictionary.popitem())
print(my_dictionary)  # a random key:value item has been removed
# If you pass an argument
# print(my_dictionary.popitem('name'))  # TypeError: popitem() takes no arguments (1 given)


# update()
# Updates keys and values in a dictionary with another set of key value pairs
my_dictionary = {
    'name': 'Saquib',
    44: 'my favourite number',
    'address': 'chadwell heath',
    'pet': 'cat'
}
my_dictionary2 = {'city': 'Karachi'}
my_dictionary2.update(my_dictionary)
print(my_dictionary2)  # {'city': 'Karachi', 'name': 'Saquib', 44: 'my favourite number', 'address': 'chadwell heath', 'pet': 'cat'}

# Delete
del my_dictionary['name']
print(my_dictionary)