# len
# Return the length (number of items) of an object. The argument may be a sequence
# (such as string, tuple, list, range or dictionary ) or a collection (such as set)

print(len('awesome'))  # 7
print(len((1, 2, 3, 4)))  # 4
print(len([1, 2, 3, 4]))  # 4
print(len(range(0, 10)))  # 10
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))  # 5

print(len({1, 2, 3, 4}))  # 4

# Note: len() actually calls the __len__() method on every object thats passed in
# eg:
print('awesome'.__len__())
# here, len calls built-in method __len__() on string object
print(len('awesome'))

# This means we can define __len__() in our own class and call the len
# methd on is object


class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50


l1 = SpecialList([1, 40, 30, 100])
print(len(l1))  # 50   len() calls __len__ on object l1
