# when n error is raised, it halts the execution and shows an error message
# We can handle the errors within the code to catch and handle the error and
# continue execution using the try-except (catch) block

#basic Fomat
try:
    foobar  # will throw a NameError as there is no variable called foobar
except:
    print('PROBLEM')  # PROBLEM
print('After the try')  # After the try

# The problem with above code is it can catch every type of error as its generic
# which means we are not able to identify what went wrog and handle it accordingly.
# Highly discouraged to just use 'except:' To catch specific error

try:
    colt
except NameError:
    print('You tried tp use a variable that was never declared')  # You tried tp use a variable that was never declared
print('After the try')  # After the try

# we can have multiple excepts to handle different errors
def divide(a, b):
    try:
        c = a/b
        return 'Ola'
    except ZeroDivisionError:
        print('Don divide by zero please')
    except TypeError:
        print('a and b must be ints or floats')
    print('Hello')

print(divide(1, 0))
# Don divide by zero please
# Hello
# None

print(divide(1, 'a'))
# a and b must be ints or floats
# Hello
# None

# We can also catch multiple exceptions in a single except by defining them in a tuple
def divide(a, b):
    try:
        c = a/b
        return 'Ola'
    except (ZeroDivisionError, TypeError) as err:
        # we can have an if statement here to check err type and handle accordingly
        print('Something ent wrong')
        print(err)
    print('Hello')

print(divide(1, 0))
print(divide(1, 'a'))

# Notice: return never gets executed. hence prints None

# We can use 'except as' to catch the actual ErrorObject which we can then access
def divide(a, b):
    try:
        c = a/b
        return 'Ola'
    except ZeroDivisionError as err:
        print(err)
        print('Don divide by zero please')
    except TypeError as err:
        print(err)
        print('a and b must be ints or floats')
    print('Hello')

print(divide(1, 0))
# division by zero
# Don divide by zero please
# Hello
# None

print(divide(1, 'a'))
# unsupported operand type(s) for /: 'int' and 'str'
# a and b must be ints or floats
# Hello
# None

# using just raise
# Please note: You can throw or raise an exception whenever it is needed (Even in the absence of the try block).
# You can do it simply by calling [raise Exception(‘Test error!’)] from your code.
# Once raised, the exception will stop the current execution as usual and will go further up in the call stack until
# handled.
