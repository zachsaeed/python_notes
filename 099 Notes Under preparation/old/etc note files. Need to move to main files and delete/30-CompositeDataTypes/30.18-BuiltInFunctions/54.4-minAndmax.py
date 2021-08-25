# min and max
# Works with individual numbers or iterators

# arguments
print(min(3, 67, 89, 2, 44))  # 2
print(max(3, 67, 89, 2, 44))  # 89

# string
print(min('3a67A89$244'))  # $
print(max('3a67A89$244'))  # a

# list
sample_list = [6, 1, 8, 2]
print(min(sample_list))  # 1
print(max(sample_list))  # 8

# It works it the same way for tuples and sets BUT returns a list
# tuple:
sample_tuple = (1, 3, 2, 4, 8, 5, 7, 6)
print(min(sample_tuple))  # 1
print(max(sample_tuple))  # 8

# set:
sample_set = {7, 4, 1, 7, 3, 6, 2, 4, }  # Note: sets cant have copies
print(min(sample_set))  # 1
print(max(sample_set))  # 7

# dictionaries (keys with same datatype)
sample_dict = {1: 'a', 3: 'c', 2: 'b'}
print(min(sample_dict))  # 1
print(max(sample_dict))  # 3
# if we use mixed keys eg
sample_dict = {1: 'a', 's': 'c', 2: 'b'}
# then we get TypeError: '<' not supported between instances of 'str' and 'int'


# key parameter

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# To get the shortest length we can pass in a generator or list comprehension of lens
print(min(len(item) for item in names))  # 3
# But to get the shortest name, it gets more complicated and we need to use the key parameter
print(min(names, key=lambda n: len(n)))  # Tim
print(max(names, key=lambda n: len(n)))  # Ollivander