# Python is dynamically-typed, which means it only checks the types of the variables you specified when you run the
# program. Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Numeric Types: int, float, complex(used in integral algebra, calculus in scientific, mathematical or electrical
#                engineering apps)
# Boolean Type:	bool (True or False values (capital T and F for python to know its a boolean))
# Text Sequence Type:	str (a sequence of unicode characters)
# Sequence Types:	list, tuple, range
# Binary Sequence Types:	bytes, bytearray, memoryview
# Mapping Type:	dict
# Set Types: set, frozenset


import decimal
import sys


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x = "Hello World"	 # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following
# constructor functions:

x = str("Hello World")  # str
x = int(20)	 # int
x = float(20.5)	 # float
x = complex(1j)	 # complex
x = list(("apple", "banana", "cherry"))	 # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)  # range
x = dict(name="John", age=36)  # dict
x = set(("apple", "banana", "cherry"))  # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)	 # bool
x = bytes(5)  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview


# type() method:
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))  # <class 'int'>


# sys.sixeof() method:
# Python has a built-in function, getsizeof, that tells us how big each different datatype is in bytes.
# To see the smallest size of each datatype:

d = {"int": 0,
     "float": 0.0,
     "complex": 0+0j,
     "dict": dict(),
     "set": set(),
     "tuple": tuple(),
     "list": list(),
     "str": "a",
     "unicode": u"a",
     "decimal": decimal.Decimal(0),
     "object": object(),
     }

# Create new dict that can be sorted by size
d_size = {}

for k, v in sorted(d.items()):
    d_size[k] = sys.getsizeof(v)

sorted_x = sorted(d_size.items(), key=lambda kv: kv[1])
print(sorted_x)
# [('object', 16),
# ('float', 24),
# ('int', 24),
# ('complex', 32),
# ('tuple', 40),
# ('str', 50),
# ('unicode', 50),
# ('list', 56),
# ('decimal', 104),
# ('set', 216),
# ('dict', 232)]
