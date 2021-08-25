# The rules governing Python code formatting are codified in a document named PEP 8
# https://www.python.org/dev/peps/pep-0008/

# to setup autopep8 as pycharm external tools see:
# https://github.com/hscgavin/autopep8-on-pycharm

# we can install autpep8 python package via pip
# https://pypi.org/project/autopep8/ (See link for installation and command line usage)
#

# Python FAQs
# https://docs.python.org/3/faq/design.html#why-can-t-raw-strings-r-strings-end-with-a-backslash
# https://towardsdatascience.com/5-python-features-i-wish-i-had-known-earlier-bc16e4a13bf4

# good for advanced notes
# https://github.com/0cjs/sedoc/blob/master/lang/python/README.md

# Note: We can use semi-colons if we have different statements in a single line eg
import pdb;  pdb.set_Trace()

# packages
# absolute vs relative imports
# https://docs.python.org/3/tutorial/modules.html#intra-package-references
# Also look at realpython and other website for article on this
# create a custom package using __init__.py and how to use the path as
# from .code and import ..code etc to import from it
# from .models import Listing when we import from within the same folder, just use .
# https://www.pythonforthelab.com/blog/complete-guide-to-imports-in-python-absolute-relative-and-more/

# ------------------------------------
# del vs __del__, destructors
# wait for answer on stack overflow
# http://foobarnbaz.com/2015/07/09/understanding-python-del-and-garbage-collection/
# https://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python
# https://www.dyclassroom.com/python/python-class-destructor-del-method
# https://www.programiz.com/python-programming/del
# https://stackoverflow.com/questions/55286028/how-does-the-python-del-function-work-without-calling-getitem
# https://stackoverflow.com/questions/53917228/deleting-the-del-method-from-an-existing-object-in-python

#--------------functions--------------------
# Monkey patching
# https://riptutorial.com/python/example/9909/monkey-patching
# https://www.pythonforthelab.com/blog/monkey-patching-and-its-consequences/

# bound and unbound methods:
# https://filippo.io/instance-monkey-patching-in-python/  (read both links to stackoverflow in article)

# functools partials

# scope
# https://realpython.com/python-scope-legb-rule/
# https://medium.com/@dannymcwaves/a-python-tutorial-to-understanding-scopes-and-closures-c6a3d3ba0937
# https://www.datacamp.com/community/tutorials/scope-of-variables-python

#colon in parameters?
# class AuthenticationForUser():
#    def __init__(self, connector: Connector):
#        self.connection = connector.connect()

#-----------Decorators------------------

# Built-in Decorators
# @Property
# https://www.programiz.com/python-programming/property

# What other decorators are available in python
# Descriptors and hence properties are only supported in new style classes.
#  https://stackoverflow.com/questions/50851359/python-property-setter-not-setting-from-instance-call
# https://realpython.com/python-descriptors/

# Type annotations
# https://dev.to/dstarner/using-pythons-type-annotations-4cfe
# https://docs.python.org/3/library/typing.html
# http://veekaybee.github.io/2019/07/08/python-type-hints/#how-does-python-handle-data-types

#------------OOP------------------------

# inspect.isclass
# https://stackoverflow.com/questions/395735/how-to-check-whether-a-variable-is-a-class-or-not

# Method overloading
# https://www.geeksforgeeks.org/python-method-overloading/
# operator overloading
# https://www.geeksforgeeks.org/operator-overloading-in-python/

# abstract class and interfaces

# ---------- Composite datatypes: -----------------
# slice method same as slicing
# https://www.programiz.com/python-programming/methods/built-in/slice

'''
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
#what does {i<:6} do?
# argv.py
import sys
print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")
'''
'''Note: The f-string syntax used in argv.py leverages the new debugging specifier in Python 3.8. To read more about this 
new f-string feature and others, check out Cool New Features in Python 3.8.
# https://realpython.com/python38-new-features/
If your Python version is less than 3.8, then simply remove the equals sign (=) in both f-strings to allow the program 
to execute successfully. The output will only display the value of the variables, not their names.'''

# + - only in sequences? - Used for set operations. Dictionaries?
# iterator mathematical functions

# in and not in(only sequences?). -Also in sets

# operators
# in and not
# https://docs.python.org/3/reference/expressions.html#in
# https://realpython.com/python-operators-expressions/#logical-operators

# for in Looping thru strings, dicts.  Sets?

# list comprehensions
# var1 = False
# print("Saquib" if var1 else "Saeed")
# file 57.15 List comprehension: return [copy(self) for i in range(other)]
# {% for key, value in state_choices.items %}
# If we dot use .items, value return initials only? Why?

# Container Protocols:
# https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html
# https://ref.readthedocs.io/en/latest/understanding_python/interfaces/existing_protocols.html
# https://subscription.packtpub.com/book/application_development/9781788293181/5/05lvl1sec56/collection-protocols
# https://stackoverflow.com/questions/43566044/what-is-pythons-sequence-protocol
# https://docs.python.org/3/reference/datamodel.html
# https://stephensugden.com/crash_into_python/Protocols.html
# https://www.youtube.com/watch?v=lTnD0lrR4jc&list=PLgPJX9sVy92wfFJzRp1IlV2k0YaLO_hfJ&index=16&t=0s
# https://docs.python.org/3.8/library/stdtypes.html#text-sequence-type-str

# default_dicts
# https://stackoverflow.com/questions/59717981/better-way-to-push-data-in-python-dictionary
# https://docs.python.org/3/library/collections.html

# buffer() is a sequence

# python collections library
# collectons module
# Counte
# Named tuple
# DefaultDict
# OrderedDict

# python arrays

# __slots__
# https://www.python-course.eu/python3_slots.php

#---------------threads-------------
#https://www.pythonforthelab.com/blog/starting-and-synchronizing-threads/
#https://www.pythonforthelab.com/blog/starting-and-synchronizing-threads/
#https://www.pythonforthelab.com/blog/handling-and-sharing-data-between-threads/
# async await
# https://realpython.com/async-io-python/

#------------ Testing -------------------
# https://semaphoreci.com/community/tutorials/mocks-and-monkeypatching-in-python

# https://www.journaldev.com/22695/python-breakpoint

# ---------libraries---------------
# libraries like random, sys, inspect, collections.abc, sys. getrefcount()

# ------------ python commands---------------
# pip

# New in python 3.5, 3.8
# https://docs.python.org/3/whatsnew/3.8.html
# https://docs.python.org/3.5/whatsnew/3.5.html

# python command line options
# https://docs.python.org/using/cmdline.html#interface-options

# passing in arguments via CLI: sys.argv[1]
# https://realpython.com/python-command-line-arguments/#the-sysargv-array

magic methods
https://medium.com/python-features/magic-methods-demystified-3c9e93144bf7
https://rszalski.github.io/magicmethods/#appendix1
https://www.geeksforgeeks.org/dunder-magic-methods-python/

# helper methods?
# enum
#class Relationship(Enum):
#    PARENT = 0
#    CHILD = 1
#    SIBLING = 2



# See answer 3. Run setup.py file to install? How and why? Is it parts of the modules topic?
# https://stackoverflow.com/questions/53049195/importing-custom-module-into-jupyter-notebook


# standard datatypes
# explain standard datatypes builtin functions
# https://docs.python.org/3.8/library/stdtypes.html

# builtins
# Edit the chapter builtins to indicate in which lectures the functions have been explained
# https://docs.python.org/3.8/library/functions.html#int
# callable()
# https://realpython.com/lessons/functions-miscellaneous/

# -----------LATER-------------------

# code practice
# loop practice:
# https://www.journaldev.com/14245/python-loop-example

# guide to c python
# https://realpython.com/cpython-source-code-guide

# metclasses
# https://realpython.com/python-metaclasses/
# https://www.python.org/doc/newstyle/
# https://www.python-course.eu/python3_road_to_metaclasses.php