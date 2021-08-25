a_int = 10
b_list = [1, 2, 3]


# -- isinstance:
# The isinstance() function is specially created to return True if an object belongs to a specific class (data type) or
# it's super/base class.
print(isinstance(a_int, int))  # True
print(isinstance(b_list, list))  # True
print(isinstance(b_list, tuple))  # False
c_tuple = (4,5,6)
print(isinstance(c_tuple, tuple))  # True
# The isinstance() also returns True if the object is an instance of the base/parent class
class A (list):
    pass

a = A()
print(isinstance(a, A))  # True
print(isinstance(a,list)) # True

# We can also pass a tuple of types/classes as the second argument and it will return True if the object/instance
# belongs to at least one of the types listed in the tuple
print(isinstance(a,(float, int, str)))  # True
print(isinstance(a,(list, tuple, dict)))  #False

# The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses
# into account.

# -- class type(object):
# The type() function returns a type object and generally the same object as returned by object.__class__
# We can then use the returned type to check whether the argument belongs to a certain type using the equalsequals
# comparison operator:
print(type(a_int) == int)  # True
print(type(b_list) == list)  # True
print(type(a_int) == float)  # False
# Therefore, type cannot be used to check for inheritance hierarchy (whether an object belongs to its base class)

# Also, if three parameters are passed to type(), it returns a new type object.
# It can be used to dynamically initialize classes or existing classes with attributes.
# It is also used to register database tables with SQL.

# - type(name, bases, dict):
# Three parameters to the type() function are:
# - name: class name which becomes __name__ attribute
# - bases: a tuple that itemizes the base class, becomes __bases__ attribute
# - dict: a dictionary which is the namespace containing definitions for class body; becomes __dict__ attribute

# For example, The folllowing two statements create identical type objects
class X:
    a = 1
X = type('X', (object,), dict(a=1))

# simple default class:
o1 = type('X', (object,), dict(a='Foo', b=12))
print(type(o1))  # <class 'type'>
print(vars(o1))
# {'a': 'Foo',
#  'b': 12,
#  '__module__': '__main__',
#  '__dict__': <attribute '__dict__' of 'X' objects>,
#  '__weakref__': <attribute '__weakref__' of 'X' objects>,
#  '__doc__': None}

# class with inheritance
class test:
    a = 'Foo'
    b = 12
o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))  # <class 'type'>
print(vars(o2))
# {'b': 12,
#  'a': 'Foo',
#  '__doc__': None}


# vars([object]):
# Returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
# Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write
# restrictions on their __dict__ attributes
# (for example, classes use a types.MappingProxyType to prevent direct dictionary updates).

# Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates
# to the locals dictionary are ignored.



