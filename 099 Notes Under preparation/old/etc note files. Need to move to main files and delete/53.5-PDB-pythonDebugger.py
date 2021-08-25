# Debugging in python
# To set breakpoints in our code, we can use pdb by inserting this line:

# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# when python encounters 'pdb.set_trace()', it pauses and in the terminal we can interact
# with values or step thru one line at a time using the following inputs:

# Common PDB Commands:
# - l (list) Shows me where I am. Sort of like a map. The arrow shows us whats next
# - n (next line) executes the line with arrow and arrow moves to next line and
#   execution pauses again
# - <variable_name> we can type variable names to see their values. If we type variable
#   that doesnt exist, it says: *** NameError: name 'firsy' is not defined
# - a (all values) prints a list of all the variables and their values
# - p (print) if <variable_name> is same as a command, eg variable a or c, typing c will run
#   command continue. To overcome this, we use p <variable_name> e.g. p c
#   Example:
#   def add_numbers(a, b, c, d):
#         import pdb; pdb.set_trace()
#         return a + b + c + d
#   add_numbers(1,2,3,4)
#   use command >>> p c i.e print c to print variable c otherwise it will think continue
#   command has been issued,
# - c (continue - finishes debugging and continue with rest of the code. preferable
#   to use over q (quit) quit
# - q (quit) Not a graceful way of quitting. Throws a wrench everywhere. Use c
#   (continue) instead
# - d (Newest frame)

# Example:
import pdb
first = "First"
second = "Second"
pdb.set_trace()  # breakpoint
result = first + second  # This line will be showed as waiting or execution
third = "Third"
result += third
print(result)
