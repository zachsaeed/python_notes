# TODO:
# https://towardsdatascience.com/my-trick-to-learning-list-comprehensions-in-python-8a54e66d98b

# list comprehension is a shorthand syntax that allows us to generate new lists by
# performing changes to each item of the list and then returning the new list
# It can be applied to lists, tuples, dictionaries, sets  and generators
# and the syntax is:
# [ <item_operation> for <item> in <list>s]

num = [1, 2, 3, 4, 5, 6]

new_num = [item*10 for item in num]
print(new_num)  # [10, 20, 30, 40, 50, 60]

# this can be done in a longer way using loops
new_num = []
for item in num:
    temp_item = item*10
    new_num.append(temp_item)

print(new_num)  # [10, 20, 30, 40, 50, 60]

# Some examples:
name = 'colt'
upper_name = [char.upper() for char in name]
print(upper_name)  # ['C', 'O', 'L', 'T'] # Note it returns a list

friends = ['saquib', 'abdul', 'faiq', 'azeem']
upper_names = [friend[0].upper() + friend[1:] for friend in friends]
print(upper_names)  # ['Saquib', 'Abdul', 'Faiq', 'Azeem']

# loop thru range()
print([num*10 for num in range(1, 6)])  # [10, 20, 30, 40, 50]

# convert items to booleans
print([bool(val) for val in [10, [], '', 1, 0]])  # [True, False, False, True, False]

# convert numbers to strings
numbers = [1, 2, 3, 4, 5, 6]
string_numbers = [str(num) for num in numbers]
print(string_numbers)  # ['1', '2', '3', '4', '5', '6']

# List comprehensions with Logic

# syntax using if
# [<item_expresion> for <item> in <list> if <boolean_expresion>]
# syntax using if else
# [<item_expresion_1> if <boolean_expresion> else <item_expresion_2> for <item> in <list>]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using if
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)  # [1, 3, 5, 7, 9]

# Using if else
# multiply with 2 if even or divide by 2 (if odd)
new_numbers = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(new_numbers)  # [0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5, 20]

# remove vowels
with_vowels = "This is so much fun!"
# Notice square brackets are optional below:
without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)  # Ths s s mch fn!

# Nesed List Comprehension
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8,  9]]

print('using nested for loops: ')
# To access / print values in nested lists,
# Either we can use nested for loops
for nested_list in nested_lists:
    for item in nested_list:
        print(item)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# or we can use list comprehensions
print('using list comprehensions: ')
[[print(item) for item in nested_list] for nested_list in nested_lists]

# multiply by 10 while keeping structure in place
abc = [[item*10 for item in nested_list] for nested_list in nested_lists]
print(abc)

#TODO see 2 more examples in vid 117

#set
# By all means, please use set() to create an empty set.
# But, if you want to impress people, tell them that you can create an empty set using literals and * with Python >= 3.5 (see PEP 448) by doing:
# >>> s = {*()}  # or {*{}} or {*[]}
# >>> print(s)
# set()
# this is basically a more condensed way of doing {_ for _ in ()}, but, don't do this.


#sets
s = set({1, 2, 3, 4, 5, 6, 7})

print({x**2 for x in s})  # {1, 4, 36, 9, 16, 49, 25}

# note: this gives us a dictionary as it has keys:
print({x:x**2 for x in s})  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

print({char.upper() for char in 'hello'})  # {'H', 'L', 'O', 'E'}
# Notice hello has duplicates and sets are unordered

string1 = 'hello'
# to see how many vowels
print(len({char for char in string1 if char in 'aeisou'})) # 2

# Dicts
# syntax
# {<key>:<value expression> for <key>, <value> in <dict>.items()}

# iterates over keys by default
# to iterate over keys and values use .items()

my_dictionary = {
    'num1': 1,
    'num2': 2,
    'num3': 3,
    'num4': 4,
    'num5': 5
}

squared_values = {key: value**2 for key, value in my_dictionary.items()}
print(squared_values)  # {'num1': 1, 'num2': 4, 'num3': 9, 'num4': 16, 'num5': 25}

squared_values2 = {num: num**2 for num in [1,2,3,4,5,6]}
print(squared_values2)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
