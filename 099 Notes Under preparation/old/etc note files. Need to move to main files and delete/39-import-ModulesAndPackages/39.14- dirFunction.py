# View the defined names in a namespace
# In this lesson, you’ll learn about the built-in function dir(). It returns a list of defined names in a namespace.
# Without arguments, it produces an alphabetically sorted list of names in the current 'local symbol table':
print(dir())
# [
#  '__annotations__', '__builtins__', '__cached__', '__doc__',
#  '__file__', '__loader__', '__name__', '__package__', '__spec__'
# ]

spam = [1, 2, 3, 4, 5]
print(spam)  # [1, 2, 3, 4, 5]
print(dir())
# [
#  '__annotations__', '__builtins__', '__cached__', '__doc__',
#  '__file__', '__loader__', '__name__', '__package__', '__spec__', 'spam'
# ]

class Extraclassy():
    pass
x = Extraclassy()
print(dir())
# [
#  'Extraclassy', '__annotations__', '__builtins__', '__cached__', '__doc__',
#  '__file__', '__loader__', '__name__', '__package__', '__spec__', 'spam', 'x'
# ]

# Note how the first call to dir() above gives several names that are automatically defined and already in the namespace
# when the interpreter starts. As new names are defined (spam, Extraclassy, x), they appear on subsequent invocations of
# dir().


# run following in a new script or restart REPL:
# This can be useful for identifying what exactly has been added to the namespace by an import statement:
import mod
print(dir())
# [
#   '__annotations__', '__builtins__', '__cached__', '__doc__',
#   '__file__', '__loader__', '__name__', '__package__', '__spec__', 'mod'
# ] # Now mod is here but individual items that are part of mod are not part of the local symbol table

print(mod.s)  # 'Computers are useless. They can only give you answers.'
mod.printy([1, 2, 3])  # arg = [1, 2, 3]

from mod import a, Classy
print(dir())
# [
#   'Classy', '__annotations__', '__builtins__', '__cached__', '__doc__',
#   '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'mod'
# ] # we can also see a and Classy
print(a)  # [100, 200, 300]

y = Classy()
print(y)  # <mod.Classy object at 0x1034a5978>

from mod import s as string
print(dir())
# [
#  'Classy', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#  '__loader__', '__name__', '__package__', '__spec__', 'a', 'mod', 'string', 'y'
# ] now we have added y and string. Classy, a and mod were alreay in the local scope table

# print(s)  # NameError: name 's' is not defined
print(string)  # 'Computers are useless. They can only give you answers.'


# run following in a new script or restart REPL:
# When given an argument that is the name of a module, dir() gives the names defined in the module:
import mod
print(dir())
# [
#  '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#  '__loader__', '__name__', '__package__', '__spec__', 'mod'
#  ]

print(dir(mod))
# [
#  'Classy', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
#  '__name__', '__package__', '__spec__', 'a', 'printy', 's'
#  ]  mod has its own symbols table which we can see above

from mod import *
print(dir())
# [
# 'Classy', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'a', 'mod', 'printy', 's'
# ]  # Classy, printy, a and s are all in the local symbols table
