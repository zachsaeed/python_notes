# The else runs if except is not entered. If except is entered, the else wont run
try:
    1/2  # Doesnt throw an error
    #1/0 # Throws an error
except:
    print('PROBLEM')
else:
    print('No Problem')  # No Problem
print('After the try')  # After the try

# No Problem
# After the try
#   if exception:
# PROBLEM
# After the try


# - finally block is always executed after leaving the try statement. The finally clause is also executed “on the way
#   out” when any other clause of the try statement is left via a break, continue or return statement
# - In case if some exception was not handled by except block, it is re-raised after execution of finally block.
# - finally block is used to deallocate the system resources.
# - One can use finally just after try without using except block, but no exception is handled in that case.
# No exception Exception raised in try block
try:
    k = 5 / 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')