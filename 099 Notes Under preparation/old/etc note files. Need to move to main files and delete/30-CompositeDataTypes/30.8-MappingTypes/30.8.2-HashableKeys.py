# Hashable objects:
# An object is hashable if it has a hash value which never changes during its lifetime. The hash value is like a
# numerical value  which can be used as a signature for that particular object.

# In python, immutable data types are hashable and  come with a built-in method for computing their hash value, which is
# called __hash__. This means mutable objects cannot be hashed.

# To look for the __hash__ function, we can either use dir():
var_tuple = (1, 2, 3, 4, 5)
dir(var_tuple)
# or the built-in hash function
#x = hash(set([1,2])) #set unhashable
x = hash(frozenset([1,2])) #hashable
#x = hash(([1,2], [2,3])) #tuple of mutable objects, unhashable
x = hash((1,2,3)) #tuple of immutable objects, hashable
#x = hash()
#x = hash({1,2}) #list of mutable objects, unhashable
#x = hash([1,2,3]) #list of immutable objects, unhashable

# Python immutable types that can be hashed (Have a built-in __hash__ method):
# int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

# - Python mutable types that cannot be hashed (Do ot have a built-in __hash__ method):
# list, dict, set, bytearray, user-defined classes

# Hash tables
# Hash tables are a type of data structure in which the address or the index value (key) of the data element is
# generated from a hash function. That makes accessing the data faster as the index value behaves like a key for the
# data value. In other words Hash table stores key-value pairs but internally, the key is generated through a hashing
# function.

# Dictionary

# - In Python, the Dictionary data types represent the implementation of hash tables. The Keys in the dictionary have to
#   satisfy the following requirements.
# 1-The keys of the dictionary need to be hashable objects (have a __hash__ method) because the dictionary uses the
#   key's hash value value internally.
# 2-The objects can be compared to other objects. (Have an __eq__() or __cmp__()  method).
#
# Dictionaries check both, hash values (which need to be different) and __eq__ (==) (which needs to return True) to
# decide whether the keys are same or different. This is done to avoid hash collisions. In other words, only if the hash
# numbers are same and == o the objects return True, the objects will be treated as a single key. Otherwise both will
# represent, unique dictionary keys

# The order of data elements in a dictionary is not fixed.
# Python dictionaries themselves are mutable, therefore unhashable
# Objects that are immutable (hashable) cannot be used as keys if they contain an immutable (Non-hashable) object eg a
# tuple containing list


print('Immutable datatype type as keys')
# 1- The hash value depends only on the data stored and not on the identity of the object itself. Therefore 2 different
#    objects of the same built-in type, and storing the same data have the same hash value
# 2-  Also, the == (__eq__) method returns true in built-in datatypes as the data is compared (not the references or id)
# Therefore, both objects will be treated as the same key if they hold the same data:
# Example:
tuple_var1 = (1, 2, 3)
tuple_var2 = (1, 2, 3)
# Different ids:
print(id(tuple_var1))  # 140697473296656
print(id(tuple_var2))  # 140697473295216
# They are indeed different objects, however, their hash values are the same:
print(tuple_var1.__hash__())  # 2528502973977326415
print(tuple_var2.__hash__())  # 2528502973977326415
# And __eq__ returns true
print(tuple_var1 == tuple_var2)  # True
# This means that if you use them as dictionary keys, they are going to be indistinguishable from each other, for
# instance:
dict_var = {tuple_var1: 'A value'}
print(dict_var[tuple_var2])  # 'A value'
# In the same way, you could have used the tuple itself:
print(dict_var[(1, 2, 3)])  # 'A value'
print(dict_var[1, 2, 3])  # 'A value'


print('Objects with same hash but unequal')
# On the other hand, if 2 objects have the same hash but are not equal, they will be treated as separate keys:
string_var = 'a'
print(string_var.__hash__())  # 12416037344
int_var = 12416037344
# Same hash values:
print(string_var.__hash__() == int_var.__hash__())  # True
# But not equal:
print(string_var == int_var)  # False
# Both string_var and int_var have the same hash value but are not equal. So, if we use them in a dictionary, they will
# be treated as separate keys:
dict_var = {string_var: 'a value'}
dict_var[int_var] = 'a second value'
print(dict_var)  # {'a': 'a value', 12416037344: 'a second value'}


print('Custom Classes objects as keys:')
# We have seen before that there are differences between mutable and immutable types in Python.
# Built-in immutable datatypes always a hash method, while mutable types don't. Also they return True when 2 objects
# with the same data are compared.
# On the other hand, custom defined classes are different. By default, all instances of custom classes will have a hash
# value defined at creation using their id so, will be different every time. But,
# 1- Unlike built-in types, two instances of the same class with same data will have two different hash values. (hash is
#    derived from their ids)
# 2- Two instances of the same class will return false when compared, as by default, __eq__ is defined to compare their
#    ids, not their data.
# Therefore they will be treated as separate keys. Example:
class MyClass:
    def __init__(self, value):
        self.value = value

my_obj = MyClass(1)
print(my_obj.__hash__())  # 8757243744113
my_obj_2 = MyClass(1)
print(my_obj_2.__hash__())  # -9223363279611078919
print(my_obj == my_obj_2)  # False
# different hashes and not equal
dict_var = {my_obj: 'my_obj'}
dict_var[my_obj_2] = 'my_obj_2'
print(dict_var)  # {<__main__.MyClass object at 0x10138bcd0>: 'my_obj', <__main__.MyClass object at 0x10138bd50>: 'my_obj_2'}

# If you run the code above, the hashes are different (derived from ids) and both objects are not equal. So they are
# treated as separate keys

print('Custom Objects with same hash values but not equal:')
# Python, as expected, allows you to define your own hash value. For example, you can alter MyClass like this:
class MyClass2:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

# If you re-run the example, you will see that both objects have the same hash value of 1. So, let's see what happens if
# we use them as the keys for a dictionary:
my_obj = MyClass2(1)
my_obj_2 = MyClass2(1)
dict_var = {my_obj: 'my_obj'}
dict_var[my_obj_2] = 'my_obj_2'
print(dict_var)  # {My Class2: 'my_obj', My Class2: 'my_obj_2'}
# What you can see is that, even if the hash value is the same, they are different objects and end up as different keys
# in the dictionary. This is because they are not equal to each other.
print(my_obj == my_obj_2)  # False

print('Custom Objects with same hash values and equal:')
# We can tweak the MyClass class in order to output True (based on their data not ids) when comparing it:
class MyClass3:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __eq__(self, other):
        return other.var == self.var

my_obj = MyClass3(1)
my_obj_2 = MyClass3(1)
my_obj_3 = MyClass3(2)
print(my_obj == my_obj_2)  # True
print(my_obj == my_obj_3)  # False

# It works as we would expect it to. If we try again with a dictionary:
dict_var = {my_obj: 'var1'}
dict_var[my_obj_2] = 'var2'
print(dict_var)  # {My Class: 'var2'}
dict_var[my_obj_3] = 'var3'
print(dict_var)  # {My Class: 'var2', My Class: 'var3'}

# Finally, we see what is that dictionaries in Python are using for defining their keys. They do not only look at the
# hash value, they also look whether the keys are the same or not. If the hashes are different or the comparision is
# false, or both, they will be assigned to separate elements instead of the same one.


# INTERVIEW
print('objects of different types with same hashes and equal to each other')
# Now you are starting to go through risky waters. If you would compare your object to something other than the MyClass
# instance (or better said, any object without a var attribute), an exception would be raised. You can also force the
# equality to be true regardless of the object you are comparing it to. So, for example:
class MyClass4:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __eq__(self, other):
        return True
# And now, we would find a strange behavior:
my_obj = MyClass4(1)
int_var = 1
print(my_obj == int_var)  # True  # my_obj's __eq__ called which always returns True
dict_var = {my_obj: 'my_obj'}
dict_var[int_var] = 'var'
print(dict_var)  # {MyClass4: 'var'}

# So now you see that if the hash and equal for both keys satisfy the dict to be tretaed as the same key, only the value
# is updated while the old key stays the same to make dictionary processing more efficient.


print('immutable types are not always immutable:')
# tuples are not always immutable. For instance, they can contain list elements...
my_tuple = ('a', 'b', [1, 2])
print(type(my_tuple))  # tuple

# Let's try using my_tuple as a dictionary key.
# First we'll create a dictionary and insert a (key, value) pair
my_dict = {}
my_dict['test'] = 'foo'
print(my_dict)  # {'test': 'foo'}

# Let's make sure that we cannot use a list element in the dictionary
my_dict[[1, 2]] = 'foo'  # TypeError: unhashable type: 'list'
# Dictionary has not changed
print(my_dict)  # {'test': 'foo'}

# Let's try inserting a tuple containing a list, as a key
my_dict[my_tuple] = 'bar'  # TypeError: unhashable type: 'list'

# This should be true for namedtuples as well.
from collections import namedtuple

TestTuple = namedtuple('TestTuple', ['field1', 'field2', 'field3'])
my_item = TestTuple('a', 'b', [1, 2])
print(type(my_item))  # __main__.TestTuple
print(isinstance(my_item, tuple))  # True
my_dict[my_item] = 'bar'  # TypeError: unhashable type: 'list'

# What's going on?
# Python dictionaries leverage hash tables. When we use a key that contains an unhashable type, i.e. a list, the
# underlying hash map cannot guarantee the key will map to the same bucket every single time. If we can't hash our key,
# we can't use it in our dictionary.
# Therefore, Python dictionaries require hashable dict keys. Having immutable keys is not enough.
