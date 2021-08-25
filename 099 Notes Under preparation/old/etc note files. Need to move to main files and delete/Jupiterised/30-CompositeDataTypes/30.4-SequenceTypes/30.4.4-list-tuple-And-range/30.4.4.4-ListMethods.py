# List methods
# To add to list: append, extend, insert
# To remove from list: clear, pop, remove
# Miscellaneous: index, count, (Available in all sequences)
# sort, reverse, join, copy

# -------------To add to list: append, extend, insert

# append( item ):
# Adds an item to the end of the list.
# Note: It takes exactly one argument. str.append(1,4) will throw an ERROR
first_list = [1, 2, True, 4]
first_list.append('saquib')
print(first_list)  # [1, 2, True, 4, 'saquib']

# extend( [ list ] ):
# Concatenates a passed list's items to the end of the current list
print('\nextend():')
second_list = ['saeed', '4', 'A', False]
first_list.extend(second_list)
print(first_list)  # [1, 2, True, 4, 'saquib', 'saeed', '4', 'A', False]


# insert( index, item ): Insert an item at a given position
print('\ninsert(): ')
first_list = [1, 2, True, 4, 'saquib', 'saeed', '4', 'A', False]
first_list.insert(2, 'Hi')
print(first_list)  # [1, 2, 'Hi', True, 4, 'saquib', 'saeed', '4', 'A', False]

first_list.insert(-1, '2nd last')
# [1, 2, 'Hi', True, 4, 'saquib', 'saeed', '4', 'A', '2nd last', False]
print(first_list)
# Note: The -ve index position is calculated on the old version of the list, therefore
# item is added second to last

# To insert last:
first_list.insert(len(first_list), 'End')
print(first_list)  # [1, 2, 'Hi', True, 4, 'saquib', 'saeed', '4', 'A', '2nd last', False, 'End']


# -------------------To remove from list: clear, pop, remove

# clear() removes all items from list
print('\nclear(): ')
first_list.clear()
print(first_list)  # []

# pop( optional_position ) removes a single item from the given position and returns it.
# If no index is specified, it removes the last item and returns it
print('\npop(): ')
first_list = [
    1,
    2,
    'Hi',
    True,
    4,
    'saquib',
    'saeed',
    '4',
    'A',
    '2nd last',
    False,
    'End']
# will pop from end:
print(first_list.pop())  # End
# [1, 2, 'Hi', True, 4, 'saquib', 'saeed', '4', 'A', '2nd last', False]
print(first_list)
# will pop from speciic index:
print(first_list.pop(5))  # saquib
# [1, 2, 'Hi', True, 4, 'saeed', '4', 'A', '2nd last', False]
print(first_list)
# first_list.pop(20) #Index Error

# remove( item_value )  Removes the first occurrence of the item from list whose value matches
# the parameter
# Note: It returns none unlike pop which returns the popped value
# Alo if the item value appears multiple times in list, it only removes
# the first occurrence
print('\nremove(): ')
first_list = [1, 2, 3, 4, 4, 4, 4]
# will remove from list:
first_list.remove(2)
print(first_list)  # [1, 3, 4, 4, 4, 4]
first_list.remove(4)
print(first_list)  # [1, 3, 4, 4, 4]
# throws a ValueError if the item is not found
# first_list.remove(9) # ValueError: list.remove(x): x not in list


#  ------------------- index, count, sort, reverse, join
# index() and count() which are common methods within all sequence types therefore, # discussed in a separate topic.

# reverse( ) reverses the elements of the list. Note: It mutates/updates the list it is called on
print('\nreverse(): ')
first_list.reverse()
print(first_list)  # [10, 9, 8, 8, 5, 7, 6, 5, 5]
# Note: Same as doing (Doesn't mutate the list.):
print(first_list[::-1])  # [5, 5, 6, 7, 5, 8, 8, 9, 10]


# sort( ) sorts the elements of the list in ascending order. (in-place) It updates the list
# it is called on
print('\nsort(): ')
first_list.sort()
print(first_list)  # [5, 5, 5, 6, 7, 8, 8, 9, 10]
second_list = sorted(['sd', 'as', 'uhki', 'wfet', 'qwer', 'fdg'])
print(second_list)  # ['as', 'fdg', 'qwer', 'sd', 'uhki', 'wfet']


# copy() -Shallow copies a list
lis1 = [1, 2, 3, 4]
# Using copy() to create a shallow copy
lis2 = lis1.copy()
# Printing new list
print("The new list created is : " + str(lis2))


