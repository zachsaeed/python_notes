# In this lesson, you’ll learn about executing a module as a script. Any .py file that contains a module is essentially
# also a Python script, and there isn’t any reason it can’t be executed like one.

# Here’s mod.py, as it was defined earlier:
''' mod.py
s = "Computers are useless. They can only give you answers."
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass
'''

# This can be run as a standalone script with the following command:
# $python3 mod.py
# There are no errors, so it apparently worked. Granted, it’s not very interesting. As it is written, it only defines
# objects. It doesn’t do anything with them, and it doesn’t generate any output.

# Let’s modify the above Python module so it does generate some output when run as a script:
''' mod2.py
s = "Computers are useless. They can only give you answers."
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

print(s)
print(a)
printy('Good Day Sir!')
x = Classy()
print(x)
'''

# Now it should be a little more interesting:
# $ python3 mod.py
# Computers are useless. They can only give you answers.
# [100, 200, 300]
# arg = Good Day Sir!
# <__main__.Classy object at 0x10f7a35f8>

# Unfortunately, now it also generates output when imported as a module:
import mod2
# Computers are useless. They can only give you answers.
# [100, 200, 300]
# arg = Good Day Sir!
# <__main__.Classy object at 0x111324748>

# This is probably not what you want. It isn’t usual for a module to generate output when it is imported. Wouldn’t it be
# nice if you could distinguish between when the file is loaded as a module and when it is run as a standalone script?
# Ask and ye shall receive!

# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
# However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'. Using this
# fact, you can see which is the case at run-time and change behavior accordingly:
''' mod3.py:
s = "Computers are useless. They can only give you answers."
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass

if (__name__ == '__main__'):
    print(s)
    print(a)
    printy('Good Day Sir!')
    x = Classy()
    print(x)
'''

# Now, if you run as a script, you get output:
# $ python3 mod3.py
# Computers are useless. They can only give you answers.
# [100, 200, 300]
# arg = Good Day Sir!
# <__main__.Classy object at 0x100a5d5f8>

# But if you import as a module, you don’t:
import mod3
print(dir())
# [
#   '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#   '__loader__', '__name__', '__package__', '__spec__', 'mod2', 'mod3'
# ]
print(__name__)  # '__main__'
print(mod3.__name__)  # 'mod3'

# Modules are often designed with the capability to run as a standalone script for testing the functionality that is
# contained within the module. This is referred to as unit testing. For example, suppose you have created a module
# fact.py containing a factorial function, as follows:
'''
def fact(n):
    return 1 if n == 1 else n * fact(n-1)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
'''
# You can treat the file as a module and import fact():
from fact import fact
fact(6)  # 720

# But you can also run it as a standalone by passing an integer argument on the command-line for testing:
# python3 fact.py 6     # 720
