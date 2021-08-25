# https://docs.python.org/3/reference/datamodel.html
# https://rszalski.github.io/magicmethods/
# https://micropyramid.com/blog/python-special-class-methods-or-magic-methods/
#
# Magic methods and attributes in Python are the special methods/variables which add
# "magic" to your class, object or function.
# Magic methods are not meant to be invoked directly by you, but the invocation
# happens internally from the class on a certain action. For example, when you add
# two numbers using the + operator, internally, the __add__() method will be called.

# Built-in classes in Python define many magic methods too. Use the dir() function
# to see the number of magic methods inherited by a class.
# For example, the following lists all the attributes and methods defined in the
# int class:
print(dir(int))

# The most common magic methods are:
# This is not a complete list as classes, instances and unctions have additional
# magic attributes/methods

# https://rszalski.github.io/magicmethods/#construction
# Construction and Initialization:
# __new__(cls, other) # Create instance. Discussed in next topic
# __init__(self, other)  # Initialises the created instance. Discussed in next topic
# __del__(self) # Destructor method called by garbage collector. Discussed ahead

# Representing your Classes:
# Magic attributes:
# __class__  # has the name of the class. Same value as as type(instance)
# __name__  # discussed ahead
# __doc__  # Returns """1st-line""" defined under class or function def. Discussed ahead

# '__init_subclass__',
# '__subclasshook__',
# '__weakref__'



# Magic Methods:
# __dir__(self)  # To get called by built-int dir() method to return a list of attributes of a class.
# __dict__  # Dictionary if instance attributes. Discussed ahead
# __repr__(self)  # Called by built-in repr() method. Discussed ahead
# __str__(self)  # Called by built-in str() method. Discussed ahead
# __format__(self, formatstr)  # Called by built-in string.format() method. Discussed ahead
# __unicode__(self)
# __hash__(self)
# __nonzero__(self)
# __sizeof__(self)

# TODO https://rszalski.github.io/magicmethods/#access
# Controlling Attribute Access
# __getattr__(self, name)
# __setattr__(self, name, value)
# __delattr__(self, name)
# __getattribute__(self, name)

# Callable Objects
# https://rszalski.github.io/magicmethods/#callable
# __call__(self, [args...])  # Create callable instance/object. Discussed ahead

# TODO https://rszalski.github.io/magicmethods/#reflection
# Reflection
# __instancecheck__(self, instance)
# __subclasscheck__(self, subclass)

# TODO https://rszalski.github.io/magicmethods/#sequence
# Making Custom Sequences
# __len__(self)
# __getitem__(self, key)
# __setitem__(self, key, value)
# __delitem__(self, key)
# __iter__(self)
# __reversed__(self)
# __contains__(self, item)
# __missing__(self, key)


# https://rszalski.github.io/magicmethods/#operators
# Boolean Operators
# __cmp__(self, other)
# __eq__(self, other)
# __ne__(self, other)
# __lt__(self, other)
# __gt__(self, other)
# __le__(self, other)
# __ge__(self, other)

# TODO https://docs.python.org/3/howto/descriptor.html
# Descriptor object
# '__get__',
# '__set__',
# '__delete__',

# TODO https://rszalski.github.io/magicmethods/#copying
# Copying
# __copy__(self)
# __deepcopy__(self, memodict={})

# https://rszalski.github.io/magicmethods/#pickling
# Pickling
# __getinitargs__(self)
# __getnewargs__(self)
# __getstate__(self)
# __setstate__(self, state)
# __reduce__(self)
# __reduce_ex__(self)



