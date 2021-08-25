# https://docs.python.org/3/reference/import.html
# As our python files get larger and larger, it is possible to break up our code into multiple files and then import
# them as/when required
# Importing is also needed for built-in modules that come with python by default and other third party/ external modules
# (after we download and install them via pip).
# Note:
# Package: directory on a filesystem containing subpackages or modules
# Module: Python file ending with .py


# ------ import <module_name>
# The simplest form is the one you already saw
# Note that this does not make the module contents directly accessible to the caller. Each module has its own private
# symbol table, which serves as the global symbol table for all objects defined in the module. So, a module creates a
# separate namespace.
# The statement import <module_name> only places <module_name> in the caller’s symbol table. The objects that are
# defined in the module remain in the module’s private symbol table.
# From the caller, objects in the module are only accessible when prefixed with <module_name> via dot notation, as
# you’ll see below.

# After the following import statement, mod is placed into the local symbol table. So, mod has meaning in the caller’s
# local context:
import mod
print(mod)  # <module 'mod' from '/Users/chris/ModulesAndPackages/mod.py'>
# But a, s, and printy() remain in the module’s private symbol table and are not meaningful in the local context:
# print(a)  # NameError: name 'a' is not defined
# print(s)  # NameError: name 's' is not defined
# printy  # NameError: name 'printy' is not defined

# To be accessed in the local context, names of objects defined in the module must be prefixed by mod:
print(mod.a) # [100, 200, 300]
print(mod.s) # 'Computers are useless. They can only give you answers.'
mod.printy('Hello')  # arg = Hello

# Several comma-separated modules may be specified in a single import statement:
# import <module_name>[, <module_name> ...]


# ------ from <module_name> import <name(s)>
# An alternate form of the import statement allows individual objects from the module to be imported directly into the
# caller’s symbol table:
# from <module_name> import <name(s)>

# Following execution of the above statement, <name(s)> can be referenced in the caller’s environment without the
# <module_name> prefix:
from mod import s, printy
print(s)  # 'Computers are useless. They can only give you answers.'
printy('Hello')  # arg = Hello

# Because this form of import places the object names directly into the caller’s symbol table, any objects that already
# exist with the same name will be overwritten:
a = ['abc', 'def', 'ghi']
print(a)  # ['abc', 'def', 'ghi']

from mod import a
print(a)  # [100, 200, 300]

# It is even possible to indiscriminately import everything from a module in one fell swoop:
# from <module_name> import *
# This will place the names of all objects from <module_name> into the local symbol table, with the exception of any
# that begin with the underscore (_) character:
from mod import *
print(s)  # 'Computers are useless. They can only give you answers.'
print(a)  # [100, 200, 300]
printy  # <function printy at 0x03B449C0>
Classy  # <class 'mod.Classy'>

# This isn’t necessarily recommended in large-scale production code. It’s a bit dangerous because you’re entering names
# into the local symbol table en masse. Unless you know them all well and can be confident there won’t be a conflict
# you have a decent chance of overwriting an existing name inadvertently.
from time import *
from asyncio import *
print('Here')
# sleep(1)  # Warning: both time and asyncio define a function sleep which behaves in very different ways.
print('After')

# However, this syntax is quite handy when you’re just mucking around with the interactive interpreter, for testing or
# discovery purposes, because it quickly gives you access to everything a module has to offer without a lot of typing.

# Therefore, it is very wise to use the first syntax that we saw earlier:
import time
import asyncio
print('Here')
asyncio.sleep(1)
print('After')
time.sleep(1)
print('Finally')

# ------ from <module_name> import <name> as <alt_name>
# It’s also possible to import individual objects but put them into the local symbol table with alternate names:
# from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]
# This makes it possible to place names directly into the local symbol table but avoid conflicts with previously
# existing names:
a = ['abc', 'def', 'ghi']
s = 'Hello There!'
from mod import s as string, a as alist
print(a)  # ['abc', 'def', 'ghi']
print(s)  # 'Hello There!'
print(string)  # 'Computers are useless. They can only give you answers.'
print(alist)  # [100, 200, 300]

# Another Example:
from asyncio import sleep as async_sleep
from time import sleep as time_sleep
print('Here')
async_sleep(1)
print('After')
time_sleep(1)
print('Finally')
# With this, we import just the modules we want, and not the entire package, but still maintain our options open by
# avoiding name clashes.

# ------ import <module_name> as <alt_name>
# You can also import an entire module under an alternate name:
# import <module_name> as <alt_name>
# Here’s what that looks like in practice:

import mod as my_module
print(my_module.a)  # [100, 200, 300]
print(my_module.s)  # 'Computers are useless. They can only give you answers.'


# ------ Import inside function definition
# Module contents can be imported from within a function definition. In that case, the import does not occur until the
# function is called:
def importer():
    from mod import printy
    printy('Hello Everyone')

print(mod)  # NameError: name 'mod' is not defined
printy  # NameError: name 'printy' is not defined

importer()  # arg = Hello Everyone

# However, Python 3 does not allow the indiscriminate import * syntax from within a function:
def importer2():
    from mod import *  # SyntaxError: import * only allowed at module level


# ----- Import Exception handling:
# Lastly, you can use a try statement with an except ImportError to guard against unsuccessful import attempts:
try:
    # Non-existent module
    import foo
except ImportError:
    print('Module not found')  # Module not found

try:
    # Existing module, but non-existent object
    from mod import bar
except ImportError:
    print('Object not found in module')  # Object not found in module
