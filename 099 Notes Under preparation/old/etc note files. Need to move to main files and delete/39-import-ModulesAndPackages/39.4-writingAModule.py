# In this lesson, you’ll learn the fundamentals of writing a module. There are three ways to define a module in Python:
# - A module can be written in Python itself.
# - A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
# - A built-in module is intrinsically contained in the interpreter, like the itertools, math, random or datetime
#   module.

# A module’s contents are accessed the same way in all three cases: with the import statement.

# Here, the focus will mostly be on modules that are written in Python. The cool thing about modules written in Python
# is that they are pretty straightforward to build. All you need to do is create a file that contains legitimate Python
# code and then give the file a name with a .py extension. That’s it! You don’t need any special syntax.

# For example, suppose you have created a file called mod.py containing the following:

s = "Computers are useless. They can only give you answers."
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

# Several objects are defined in mod.py:
# s: a string
# a: a list
# printy(): a function
# Classy: a class

# Assuming mod.py is in an appropriate location, which you’ll learn more about shortly, these objects can be accessed by
# importing the module as follows:
import mod

print(mod.a)  # [100, 200, 300]
print(mod.s)  # 'Computers are useless. They can only give you answers.'
mod.printy('What is up!')  # arg = What is Up!
x = mod.Classy()
print(x)  # <mod.Classy object at 0x03C181F0>
