# A normal function in python


def square(num): return num * num
print(square(9))  # 81
# A name function can be assigned to a variable and then called again with new variable name
sq = square
print(sq(2))  # 4

print(square.__name__)  # square
print(sq.__name__)  # square

# A lambda function, (also called anonymous function) has no name
square2 = lambda num: num * num
print(square2(7))  # 49
# It is NOT usually used in this manner by assigning to a variable. This is just an
# example to show you

# A lambda with no params
what = lambda: print('What!')
what()  # what!

# A lambda function with 2 params
add = lambda a, b: a+b
print(add(10, 30))  # 40

print(square2.__name__)  # <lambda>
print(add.__name__)  # <lambda>


# Lambda functions are used when you need to pass a function into another function
# as an argument and that passed function is unique and never re-used again.
# NOTE: We can pass in a named function by name too.


# Note: Lambdas are not widely used. There are vasa blog posts online where people
# argue they shouldn't be used, removed from python 3 or there should be another solution.
# The best use is in map filter and reduce functions
