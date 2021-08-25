# In this lesson, you’ll learn about the module search path. Continuing with the example from the previous lesson, take
# a look at what happens when Python executes the following statement:
import mod
print(mod.a)  # [100, 200, 300]
print(mod.s)  # 'Computers are useless. They can only give you answers.'

# When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled
# from the following sources:

# 1- sys.modules - A cache where everything that was previously imported (in another script) is kept
# 2- Python Standard Library - This is where os, json and csv etc are kept. Anything that is not pip installed and
#    comes with python is generally kept here. List of built-in modules: https://docs.python.org/3/py-modindex.html
# 3- sys.path - This is a list of dirs which usually includes the current directory.
#    - It will first start by searching in the current directory from which the input script was run, or the current
#      directory if the interpreter is being run interactively
#    - Then it will move to the directories where packages are installed (for example, when you do pip install numpy).
#      Any local files you write for your app should be located here and this is where 'absolute' and 'relative' imports
#      become very important. These paths mainly comprise of:
#      -  The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for
#         PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
#         https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
#      -  An installation-dependent list of directories configured at the time Python is installed
# 4- ModuleNotFoundError: After checking all of the above, if a module is still not found, you get ths error. It
#    generally means you made a typo, didnt install something, or directed python o the wrong area

# Note: The above order is very specific and can have a couple of security concerns. sys.modules is a writable cache, so
# there is a chance, unexpected code can be imported into your project. For example, dll hijacking on windows machine is
# a similar concept

# In the Python variable sys.path, the search paths are accessible which is obtained from a module named sys:
import sys
print(sys.path)
# [
#   '',
#   '/Library/Frameworks/Python.framework/Versions/3.7/bin',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'
# ]

# Note: The exact contents of sys.path are installation-dependent. The above code block will almost certainly look
# slightly different on your computer. The operating system used in this lesson is macOS. If you would like to see what
# the path structure looks like in a Windows environment, check out the original article that this course is based on.

# So, to ensure that your module is found, you need to do one of the following:
# - Put mod.py in the directory where the input script is located, or the current directory if interactive
# - Modify the PYTHONPATH environment variable to contain the directory where mod.py is located before starting the
#   interpreter.
#   - Or put mod.py in one of the directories already contained in the PYTHONPATH variable.
# - Put mod.py in one of the installation-dependent directories, which you may or may not have write-access to,
#   depending on the OS.
# - There is also one additional option: You can put the module file in any directory of your choice and then modify
#   sys.path at run-time so that it contains that directory. For example, in this case, you could put mod.py in
#   directory /Users/chris/ModulesAndPackages and then issue the following statements:
sys.path.append(r'/Users/chris/ModulesAndPackages')
print(sys.path)
# [
#   '',
#   '/Library/Frameworks/Python.framework/Versions/3.7/bin',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
#   '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages',
#   '/Users/chris/ModulesAndPackages'
#   ]

import mod
print(mod.s)  # 'Computers are useless. They can only give you answers.'

# Once you’ve imported a module, you can determine the location where it was found with the module’s __file__ attribute:
import mod
print(mod.__file__)  # /Users/saquib/cloudSync/GoogleDrive/dev/python/40-import-ModulesAndPackages/mod.py

import re
print(re.__file__)  # '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/re.py
# Above path created when installing python

# The directory portion of __file__ should be one of the directories in sys.path to be importable. If not then add it
# via sys.path.append(r'/Users/chris/ModulesAndPackages') before the import statement. (Not good practice)
