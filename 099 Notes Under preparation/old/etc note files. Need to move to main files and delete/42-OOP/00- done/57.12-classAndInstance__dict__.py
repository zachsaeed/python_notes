# INTERVIEW REVISION
# NOTE:
# - instance variables are stored in the object dictionary whereas static variables are
#   stored in the class dictionary
# - When you try access a variable in a object, Python will look first in the object,
#   if it is not there then it looks in class dict.


class Test:

    # static/class variable: (Note, i is defined in 2 places, As a class and as an instance variable)
    i = 'I am a class variable'
    j = 'I am the second class variable'

    def __init__(self, a, b, c):
        # instance variables:
        self.i = 'I am an instance variable'
        self.a = a
        self.b = b
        self.c = c

    # You can access class variable with self. But, in case you have an instance variable,
    # with the same name, you will be accessing the instance variable when you use self as
    # it is shadowing the class variable:
    def print_j(self):
        print(self.j)  # I am the second class variable

    def print_i(self):
        print(self.i)  # I am an instance variable

    def print_static_i(self):
        print(Test.i)  # I am a class variable


print(Test.__dict__)
# Prints the class dictionary:
# {
#   '__module__': '__main__',
#   'i': 'I am a class variable',
#   '__init__': <function Test.__init__ at 0x0373E588>,
#   '__dict__': <attribute '__dict__' of 'Test' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Test' objects>,
#   '__doc__': None}

test_instance = Test(1, 2, 3)
print(test_instance.__dict__)
# Prints the instance dictionary:
# {'i': 'I am an instance variable', 'a': 1, 'b': 2, 'c': 3}

# Note: When you try access a variable in a object, Python will first look in the
# object dictionary. If it is not there then it looks in class dict.
print(Test.i)  # I am a class variable
print(test_instance.i)  # I am an instance variable

test_instance.print_j()  # I am the second class variable
test_instance.print_i()  # I am an instance variable
test_instance.print_static_i()  # I am a class variable

# INTERVIEW REVISION
# NOTE: In Python, variables can be created dynamically.
# When we access j via instance and class, it gives us the static j variable
print(Test.j)  # I am the second class variable
print(test_instance.j)  # I am the second class variable
# In this method self points to the class variable:
test_instance.print_j()   # I am the second class variable

# However, when we assign a value to j via instance name, it doesnt assign it to the static j variable. Instead,
# creates a new j instance variable
test_instance.j = 'I am a new instance variable'
print(Test.j)  # I am the second class variable
print(test_instance.j)  # I am a new instance variable
# In this method self points to the instance variable:
test_instance.print_j()   # I am a new instance variable

# Eventually, you will learn that Python classes are instances and therefore objects
# themselves, which gives new insight to understanding the above.

# https://stackoverflow.com/questions/68645/are-static-class-variables-possible-in-python
# https://stackoverflow.com/questions/44460724/can-i-access-class-variables-using-self
# https://stackoverflow.com/questions/3434581/accessing-a-class-member-variables-in-python