# List:
# We can iterate through lists using both for-in and while loops

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'orange', 'pink']

# Using for in
for color in colors:
    print(color)

# We can also access with index using for-in loop
for i in range(len(colors)):
    print(f"color at index no {i} is: {colors[i]}")


# Using while
index = 0
while index < len(colors):
    print(f"color at index no {index} is: {colors[index]}")
    index += 1

# As you can see for-in is a better and shorter iterator for lists


# Tuples
# can use a for loop to iterate over tuples just like a list
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
    print(month)


# while loop just like a list
last_month_index = len(months) - 1
iter_index = 0
while iter_index <= last_month_index:
    print(months[iter_index])
    iter_index += 1


#Dictionaries
my_dictionary = {
    'name': 'Saquib',
    44: 'my favourite number',
    'address': 'chadwell heath',
    'pet': 'cat'
}

# To access each and every value, we can loop through dictionaries using the following methods
# dict.values()
# dict.keys()
# dict.items()
# They all return a view rather than a list. We need to wrap them in list() to get a list
# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects

# dict.values()
print(my_dictionary.values())
# returns the view: dict_values(['Saquib', 'my favourite number', 'chadwell heath', 'cat'])
for value in my_dictionary.values():
    print(value)
# Saquib
# my favourite number
# chadwell heath
# cat


# dict.keys()
print(my_dictionary.keys())
# returns the view: dict_keys(['name', 44, 'address', 'pet'])
for key in my_dictionary.keys():
    print(key)
# name
# 44
# address
# pet


# dict.items()
print(my_dictionary.items())
# returns the view:
# dict_items([('name', 'Saquib'), (44, 'my favourite number'), ('address', 'chadwell heath'), ('pet', 'cat')])
# Not: that dict_item view shows a list of tuples
for key, value in my_dictionary.items():  # Note: we loop through both key, value at each iteration
    print(f"key is {key}, value is {value}")
# key is name, value is Saquib
# key is 44, value is my favourite number
# key is address, value is chadwell heath
# key is pet, value is cat

# dict views
# keys and values are iterated over in the same order (insertion order)
# scroll slightly down
# https://docs.python.org/3.8/library/stdtypes.html#dictionary-view-objects

#sets
s={1,2,3,4,5}
for s_item in s:
    print(s_item)


# Test:
# please confirm. looks like for x in y:   y eeds to be sequence of tuples ad x can be structured according to each
# element (tuple)
# Example
upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']
for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):
    print(f'{i}: {upper} and {lower}.')
# 1: A and a.
# 2: B and b.
# 3: C and c.
# 4: D and d.
# 5: E and e.
# 6: F and f.

# Note: In the above code:
print(list(zip(upperCase, lowerCase)))  # [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f')]
print(list(enumerate(zip(upperCase, lowerCase), 1)))  # [(1, ('A', 'a')), (2, ('B', 'b')), (3, ('C', 'c')), (4, ('D', 'd')), (5, ('E', 'e')), (6, ('F', 'f'))]


Mydictionary = {'a':1, 'b':2, 'c':3, 'd':4}
print(Mydictionary.items())
# Doesnt work:
#for key:value in Mydictionary:
#    print(key, value)
