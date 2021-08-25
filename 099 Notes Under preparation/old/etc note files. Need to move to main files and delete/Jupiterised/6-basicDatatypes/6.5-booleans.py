# Python 3 provides a Boolean data type. Objects of Boolean type may have one of two values, True or False:
bool_var1 = True
print(type(bool_var1))  # <class 'bool'>

bool_var2 = bool(False)
print(type(bool_var2))  # <class 'bool'>

# As you will see in upcoming tutorials, expressions in Python are often evaluated in Boolean context, meaning they are
# interpreted to represent truth or falsehood. A value that is true in Boolean context is sometimes said to be “truthy,”
# and one that is false in Boolean context is said to be “falsy.” (You may also see “falsy” spelled “falsey.”)

# Non-Boolean objects can be evaluated in Boolean context as well and determined to be true or false.
# You will learn more about evaluation of objects in Boolean context when you encounter logical operators in the
# upcoming tutorial on operators and expressions in Python.