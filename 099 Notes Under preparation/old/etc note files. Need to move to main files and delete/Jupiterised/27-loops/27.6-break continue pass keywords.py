# https://www.tutorialspoint.com/python/python_loop_control.htm
# The break Statement:
# break statement terminates the current loop and resumes execution at the next
# statement, just like the traditional break found in C.
# The most common use for break is when some external condition is triggered requiring
# a hasty exit from a loop.
# The break statement can be used in both while and for loops.
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)
# Current Letter : P
# Current Letter : y
# Current Letter : t

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break
# Current variable value : 10
# Current variable value : 9
# Current variable value : 8
# Current variable value : 7
# Current variable value : 6


# The continue Statement:
# continue statement returns the control to the beginning of the while/for loop. The
# continue statement rejects all the remaining statements in the current iteration
# of the loop and moves the control back to the top of the loop.
# It can be used in both while and for loops.
for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)
# Current Letter : P
# Current Letter : y
# Current Letter : t
# Current Letter : o
# Current Letter : n

var = 10                    # Second Example
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Current variable value :', var)
# Current variable value : 9
# Current variable value : 8
# Current variable value : 7
# Current variable value : 6
# Current variable value : 4
# Current variable value : 3
# Current variable value : 2
# Current variable value : 1
# Current variable value : 0


# The pass Statement:
# pass statement is used when a statement is required syntactically but you do
# not want any command or code to execute.

# The pass statement is a null operation; nothing happens when it executes. The
# pass is also useful in places where your code will eventually go, but has not
# been written yet (e.g., in stubs for example):

for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)

# Current Letter : P
# Current Letter : y
# Current Letter : t
# This is pass block
# Current Letter : h
# Current Letter : o
# Current Letter : n

# The preceding code does not execute any statement or code if the value of letter
# is 'h'. The pass statement is helpful when you have created a code block but it
# is no longer required.
# You can then remove the statements inside the block but let the block remain with
# a pass statement so that it doesn't interfere with other parts of the code.


# Breaking outer loops
# Many popular programming languages support a labelled break statement. It’s mostly
# used to break out of the outer loop in case of nested loops. However, Python doesn’t
# support labeled break statement.
# PEP 3136 was raised to add label support to break statement. But, it was rejected
# because it will add unnecessary complexity to the language. There is a better
# alternative available for this scenario – move the code to a function and add the
# return statement.
