# INTERVIEW REVISION
#https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference?rq=1

# https://www.pythonforthelab.com/blog/mutable-and-immutable-objects/

# We already know that if we have two mutable objects with the same id it means that they are the same object. If we
# change one, you will change the other.
#
# This also applies when working with functions that take mutable objects as arguments. Imagine that you develop a
# function that takes as input a list, divides all of its arguments by 2 and then returns the average.
# The function would look like this:

def divide_and_average(var):
    for i in range(len(var)):
        var[i] /= 2
    avg = sum(var)/len(var)
    return avg

# It is very interesting to see what happens when you use this function:

my_list = [1, 2, 3]
print(divide_and_average(my_list))  # 1.0
print(my_list)  # [0.5, 1.0, 1.5]

# When you execute the function, you are actually changing the values of the variable my_list. This is very powerful
# because it allows you to change the elements of a list in-place while you are returning a different element. Sometimes
# however, you don't want to do this and want to preserve the value of the original list. It may seem like a good idea
# to create a new variable within the function and use that instead.

# For example:

def divide_and_average(var1):
    var = var1
    # [...]

# However, you will see that this doesn't change the output. As we saw earlier, the identity of var and of var1 would be
# the same. Therefore, you can make a copy of your object using the copy module:
import copy

def divide_and_average(var1):
    var = copy.copy(var1)
    # [...]

# And now you will see that the original my_list variable is not altered. What we have just done is called a shallow
# copy of an object. It is also possible to perform a deep copy, but its implications are left for a different article.

# Note: If it were an immutable object, it would have created a new object when making chnges to it anyway. So this only
# applies to mutable objects
