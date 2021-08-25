# importing custom modules / Our own code
# In python we are able to structure different parts of our code into different files, and importing them where ever
# required, making the code much handier to maintain.

# Simplest example (Under the folder '39.8.2-code') is in first.py:
def first_function():
   print('This is the first function')

# In second.py, let's put the following code:
from first import first_function
first_function()
# To avoid conflicts in 'second.py' you can also do:
# from first import first_function as ff


# Importing rom Folders:
# We can also organise our code into folders. Example: folder called module_a with third.py
# .
# ├── first.py
# ├── module_a
# │   └── third.py
# └── second.py

# third.py has code:
def third_function():
   print('This is the third function')

# We can import this function in second.py using:
from module_a.third import third_function
# Note: We specified the folder, in this case, module_a and then we referred to the file with a dot: . We ended up
# having module_a.third, and we stripped the .py.

# Now that we kow the basic of importing, we will now have a look at absolute vs relative imports
