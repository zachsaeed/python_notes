# INTERVIEW REVISION
# Single and double underscores have a meaning in Python variable and method names.
# There are five underscore patterns:

# Single Leading Underscore: _var  (Private method / attribute)
# Single Trailing Underscore: var_ (Avoid conflict with keywords)
# Double Leading Underscore: __var (Name mangling)
# Double Leading and Trailing Underscore: __var__ (Dunder methods)
# Single standalone Underscore: _ (temporary or insignificant)

# Single Leading Underscore: _var  (Private method / attribute)
# _name: There are no private method in python. Convention is to start private method
# name with an underscore. This indicates that it is for internal use and  is treated
# as non-public. Python does not impose any restrictions on accessing a variable and it
# is upto the programmer.

# Single Trailing Underscore: var_ (Avoid conflict with keywords)
# Python has some default keywords which we can not use as the variable name. To avoid
# such conflict with Python keywords or built-ins. we use underscore after the name.
# eg class_, def_ return_, break_


# Double Leading Underscore: __var (Name mangling)
# A Double Leading Underscore causes the Python interpreter to rewrite the attribute
# name to avoid conflicts of attribute names between classes. The interpreter replaces
# the double prefix underscore name with _ClassName__msg(called name mangling) as a
# way to ensure that the name will not overlap with a similar name in subclasses.
# Its sole purpose is to make this method or attribute, particular to this class so
# that when we inherit from this class, the subclass can have its own __msg and we dont
# want them to conflict. See 9.6 code example:
# https://docs.python.org/3/tutorial/classes.html#private-variables
class Person:

    def __init__(self):  # dunder method which python will automaically call during instantiation
        self.name = "Saquib"
        # private method which convention says should only be called within the
        # object
        self._secret = "hi" # Private
        self.__msg = "I like turtles!"  # python will name mangle this variable

    def doorman(self, guess):
        if guess == self._secret:  # correct usage as it needs to be treated as private
            print('Let them in')


p = Person()
print(p.name)  # Saquib

# prints hi but as per convention, do not invoke it here (outside the instance)
print(p._secret)

# print(p.__msg)  # AttributeError: 'Person' object has no attribute '__msg'
print(p._Person__msg)  # I like turtles!
# The sublcass of Person can have its own __msg which will be mangled by python to
# <_subclass__msg> and will not conflict wih super class's __msg (_Person__msg)


# Double Leading and Trailing Underscore: __var__ (Dunder methods)
# Names surrounded by a double underscore prefix and postfix are called Magic methods
# or dunder("Double UNDERscore").
# Convention defines that we only define dunder methods for methods that mean
# something for python. i.e for methods that python looks for automatically like
# __init__(), __len__, __repr__, __add__
# You can use the dir() function to see the number of magic methods inherited by a
# class.

# Single standalone Underscore: _ (temporary or insignificant)
# Per convention, a single standalone underscore is sometimes used as a name to
# indicate that a variable is temporary or insignificant.
# For example, in the following loop, we don’t need access to the running index and
# we can use “_” to indicate that it is just a temporary value:
for _ in range(2):
    print('Hey there...')

# Hey there...
# Hey there...

# Again, this meaning is per convention only and there’s no special behavior triggered
# in the Python interpreter.

# Note: Apart from use as a temporary variable, The underscore is returning the last value
# that was evaluated by the interpreter. This means you can access some computation
# after the execution and later store it into a variable and use it for something else:
# >>> 10+20
# 30
# >>> _
# 30
# >>> _+10
# 40



