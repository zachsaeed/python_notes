# INTERVIEW REVISION
# http://effbot.org/zone/default-values.htm
# https://www.pythonforthelab.com/blog/mutable-and-immutable-objects/

# This is a common mistake that beginners often make. Even more advanced programmers make this mistake if they don't
# understand Python names.

# What causes the confusion is the behaviour you get when you use a “mutable” object as a default value; that is, a
# value that can be modified in place, like a list or a dictionary. For example:
def increase_values(var1=[1, 1], value=0):
    value += 1
    var1[0] += value
    var1[1] += value
    return var1


print(increase_values())  # [2, 2]
print(increase_values())  # [3, 3]

# As you can see, the same list object's items get added by 1 everytime. If you look at the list identity, you’ll see
# that the function keeps returning the same object:
print(id(increase_values()))  # 4304224736
print(id(increase_values()))  # 4304224736


# The reason is simple: the function keeps using the same object, in each call. The modifications we make are “sticky”.

# Python creates/evaluates the default list and the default value only once at function definition time ie when the
# 'def' statement they belong to is executed.

# Note that “def” is an executable statement in Python, and that default arguments are evaluated in the “def”
# statement’s environment. If you execute “def” multiple times, it’ll create a new function object (with freshly
# calculated default values) each time. The following code shows that default argumets are executed at function
# definition:

def a():
    print("a executed")
    return []


def b(x=a()):  # a() being a default param is evaluated at function definition time
    x.append(5)
    print(x)
# prints: a executed

b()  # [5]
b()  # [5, 5]


# Everytime you call the function, you use the same default values. Since the default value of 'var1' is mutable, it
# uses the same object for all successive calls of the function whereas, the param 'value' is immutable, and therefore
# it will be preserved over time.


# The next logical question is how can you prevent this from happening.
# Use a placeholder value of immutable type as a default argument (You can use None, for instance) for functions and
# then create the mutable default value at run time instead (inside the function):

def increase_values(var1=None, value=0):
    if var1 is None:
        var1 = [1, 1]
    # ...

# If you need to handle arbitrary objects (including None), you can use a sentinel object:
sentinel = object()

def myfunc(value=sentinel):
    if value is sentinel:
        value = 'expression'
    # use/modify value here


# Uses of mutable defaults
# Imagine the case where you would like to perform a computationally expensive calculation, but you don't want to run
# twice the function with the same input and use a cache of values instead. You could do the following:

def calculate(var1, var2, cache={}):
    try:
        value = cache[var1, var2]
    except KeyError:
        value = 'expensive_computation(var1, var2)'
        cache[var1, var2] = value
    return value
# When we run calculate for the first time, there will be nothing stored in the cache dictionary, but if we execute the
# function more than once, cache will start changing, appending the new values to it. If we run calculate again with the
# same arguments, they are going to be present and their known value will be returned. Notice that we are leveraging the
# exception handling in order to avoid checking explicitly whether the combination of values already exists in memory.
