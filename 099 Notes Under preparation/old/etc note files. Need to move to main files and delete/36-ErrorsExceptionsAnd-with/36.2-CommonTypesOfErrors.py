# For full list: https://docs.python.org/3/library/exceptions.html
# Some of the common types are:

# SyntaxError: invalid syntax
# Occurs when python encounters incorrect syntax / typo (Something it cannot parse)
# def abc:
# None = 1
# return

# NameError: name 'var1' is not defined
# Occurs when a cariable is not defined ie it has not been assigned before its use
# var1

# TypeError: <description>
# Mismatch of datatype, when operations functions are applied to the wrong type
# (Python cannot interpret an operation on two data types)
# len(5)  # TypeError: object of type 'int' has no len()
# "awesome" + []  # TypeError: can only concatenate str (not "list") to str
# 3 + 's'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# int([10, 20])  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

# ValueError: <description>
# Occurs when a built-in operation or function receives an argument that has the right
# type but inappropriate value
# int("foo")  # ValueError: invalid literal for int() with base 10: 'foo'

# IndexError: <itertype> index out of range
# Occurs when you try to access an element in a list/String using an invalid index (ie
# One that is outside the rage of the list or string)
# list1 = [1,2]
# print(list1[2])  # IndexError: list index out of range
# string1 = 'Saquib'
# print(string1[20])  # IndexError: string index out of range

# KeyError: <key_name>
# Occurs with dictionaries. When you try to access a key which doesnt exist
# dict1 = {'a':1, 'b':2}
# print(dict1['d'])  # KeyError: 'd'



# AttributeError: '<classType>' object has no attribute '<attributeName>'
# When a variable doea not have an attribute
"awesome".foo  # AttributeError: 'str' object has no attribute 'foo'
# ['a', 10, '3'].hello()  # AttributeError: 'list' object has no attribute 'hello'

