# The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
# They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view
# reflects these changes.
# Dictionary views are now reversible.

first_dictionary = {"a": 1, "b": 2, "c": 3}
# for key, value in first_dictionary.items():
#     print(f"Key {key} with value {value}")

dict_keys = first_dictionary.keys()
print(type(dict_keys))  # <class 'dict_keys'>
print(dict_keys)  # dict_keys(['a', 'b', 'c'])

dict_values = first_dictionary.values()
print(type(dict_values))  # <class 'dict_values'>
print(dict_values)  # dict_values([1, 2, 3])

dict_items = first_dictionary.items()
print(type(dict_items))  # <class 'dict_items'>
print(dict_items)  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# when the dictionary changes, the view reflects these changes dynamically.
my_dictionary = {"d": 4}
first_dictionary.update(my_dictionary)

print(dict_keys)  # dict_keys(['a', 'b', 'c', 'd'])
print(dict_values)  # dict_values([1, 2, 3, 4])
print(dict_items)  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# INTERVIEW:
print(first_dictionary.values() == first_dictionary.values())  # False
print(first_dictionary.values().__eq__(
    first_dictionary.values()))  # NotImplemented
# This is only the case with .values(). .keys and .items have the __eq__
# method implemented


# - dict_key view objects are set-like since their entries are unique and hashable.
# - dict_items view objects are only set like if all values are hashable, ie the (key, value) pairs are unique and
#   hashable
# - dict_value view objects are not treated as set-like since the entries are generally not unique. (2 different keys
#   may have the same value)
# - When a set operation is applied to views, it returns a set

# For set-like views, all of the operations defined for the abstract base class collections.abc.Set are available
# (for example, ==, <, or ^).


# keys():
# Dictionary keys are always hashable, so set operations are always
# available on the dict_keys view object.
d1 = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
d2 = {'key3': 'value3-new', 'key5': 'value5'}

# All keys (set union)
# To get all keys from multiple dictionaries, you can use the set union.
# {'key5', 'key3', 'key2', 'key1'}  # this is a set, not a dict
print(d1.keys() | d2.keys())
# You can use the same approach to combine dict_items and merge dictionaries.

# Keys in common (set intersection)
# The keys common to two dictionaries can be determined using set
# intersection (&).
keys = d1.keys() & d2.keys()
print(keys)  # {'key3'}    # this is a set, not a dictionary
# You could use the resulting set to filter your dictionary using a
# dictionary comprehension.
print({k: d1[k] for k in keys})  # {'key2':'value2', 'key1':'value1'}

# Unique keys (set difference)
# To retrieve keys unique to a given dictionary, you can use set difference (-). Keys from the right hand dict_keys are
# removed from the left, resulting in a set of the remaining keys.
print(d1.keys() - d2.keys())  # {'key1', 'key2'}

# Unique keys from both (set symmetric difference)
# If you want items unique to both dictionaries, the set symmetric difference (^) returns this. The result is items
# unique to both the left and right hand of the comparison.
print(d1.keys() ^ d2.keys())  # {'key5', 'key2', 'key1'}


# items()

# If both the keys and values of a dictionary are hashable, the dict_items view will support set-like operations.
# If the values are not hashable all of these2 operations will all raise a
# TypeError.

# Merge (set union)
# You can use set union operations to merge two dictionaries.
d1 = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
d2 = {'key3': 'value3-new', 'key5': 'value5'}
d3 = {'key4': 'value4', 'key6': 'value6'}
print(dict(d1.items() | d2.items() | d3.items()))
# {'key1':'value1', 'key2':'value2', 'key3':'value3-new', 'key5':'value5', 'key4':'value4', 'key6':'value6'}
# Since it is quite common for dictionary values to not be hashable, you will probably want to use one of the other
# approaches for merging dictionaries instead.

# Common entries (set intersection)
# The items common to two dictionaries can be determined using set intersection (&). Both the key and value must match —
# items are compared as (key, value) tuples.
d1 = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
d2 = {'key1': 'value1', 'key5': 'value5'}
# {('key1', 'value1')}    # this is a set, not a dict
print(d1.items() & d2.items())

# Unique entries (set difference)
# To retrieve items unique to a given dictionary, you can use set difference (-). Items from the right hand dict_keys
# are removed from the left, resulting in a set of the remaining item
# (key, value) tuples.
d1 = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
d2 = {'key3': 'value3-new', 'key5': 'value5'}
# {('key3', 3), ('key2', 'value2'), ('key1', 'value1')}
print(d1.items() - d2.items())

# Unique entries from both (set symmetric difference)
# If you want items unique to both dictionaries, the set symmetric difference (^) returns this. The result is item (key,
# value) tuples unique to both the left and right hand of the comparison.
d1 = {'key1': 'value1', 'key2': 'value2', 'key3': 3}
d2 = {'key3': 'value3-new', 'key5': 'value5'}
# {('key2', 'value2'), ('key5', 'value5'), ('key1', 'value1'), ('key3'
print(d1.items() ^ d2.items())
