# List is just an ordered collection or grouping of items. (called arrays in other
# languages)

# Creating lists:
# 1- Using square brackets
tasks = ["install python", "Learn python", "Take a break"]
demo_list = ["a", 1, True, 23, 0.3456]  # items can be different types
# 2- or using the built-in method
fruit_list = list(("apple", "banana", "cherry"))
# 3- or we can use range()  if we want a sequence of numbers. range is not a list but and iterator.
# It can be converted to list
number_seq = list(range(1, 4))
print(number_seq)  # [1, 2, 3]

# Length
print(len(demo_list))  # 5


# INTERVIEW
# -- Multiple variable assignment using Lists
# We can also use a list to assign each item to variables in a single line
bottle, case, bag = ['A', 1.5, "Zach"]
print(bottle)
print(case)
print(bag)
# same as doing
var1, var2, var3 = 'a', 'b', 'c'
print(var1)
print(var2)
print(var3)

# @TODO ???
memo = {}
memo['a', 'b', 'c'] = (44, 33, 22)
print(memo)
print(memo['a', 'b', 'c'])

# INTERVIEW
# -- Swapping List values
names = ['syed', 'saquib', 'saeed']
# We can swap element value using indexes.
# Uses: sorting, shuffling
names[0], names[1] = names[1], names[0]
print(names)  # ['saquib', 'syed', 'saeed']
