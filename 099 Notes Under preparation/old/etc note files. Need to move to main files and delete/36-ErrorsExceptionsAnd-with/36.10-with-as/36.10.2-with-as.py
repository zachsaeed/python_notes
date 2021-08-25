# INTERVIEW REVISION
# with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies
# the management of common resources like file streams. Observe the following code example on how the use of with
# statement makes code cleaner.

# file handling

# 1) without using with statement
# An exception during the file.write() call in the first implementation can prevent the file from closing properly which
# may introduce several bugs in the code, i.e. many changes in files do not go into effect until the file is properly
# closed
file = open('file_path', 'w')
file.write('hello world !')
file.close()


# 2) without using with statement with try except/finally blocks
# takes care of all the exceptions but using the with statement makes the code compact and much more readable.
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()


# 3) using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')
# Notice that unlike the first two implementations, there is no need to call file.close() when using with statement. The
# with statement itself ensures proper acquisition and release of resources. Thus, with statement helps avoiding bugs
# and leaks by ensuring that a resource is properly released when the code using the resource is completely executed.

# The with statement is popularly used with file streams, as shown above and with Locks, sockets, subprocesses and
# telnets etc.
