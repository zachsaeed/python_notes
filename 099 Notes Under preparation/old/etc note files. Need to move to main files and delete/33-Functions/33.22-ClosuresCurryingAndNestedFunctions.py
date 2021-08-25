# Note: check named funciton scope

# Both closure and currying used the cocept of nested fuctions

print('Closures: ')
# Closure:
# A closure is a way of keeping alive a variable even when the function has
# returned. So, in a closure, a function is defined along with the environment.
# In Python, this is done by a nested function inside the encapsulating function
# and then returning the underlying function.
# So, by definition, a closure ( also lexical closure or function closure) is a
# persistent scope which holds on to local variables even after the code execution
# has moved out of that block.


def add_5():
    five = 5

    def add(arg):  # nested function
        return arg + five
    return add


if __name__ == '__main__':
    closure1 = add_5()
    print(closure1(1))  # output 6
    print(closure1(2))  # output 7

# Even though add_5() has finished execution, and returned a function, the value = 5
# is still alive in the returned function.


print('Currying: ')
# Currying is when you break down a function that takes multiple arguments into a series
# of functions that each take only one argument.


def add(a, b):
    return a + b


print(add(3, 4))  # 7
# This is a function that takes two arguments, a and b, and returns their sum.
# We will now curry this function:


def add1(a):
    def add2(b):
        return a + b
    return add2


# This is a function that takes one argument, a, and returns a function that
# takes another argument, b, and that function returns their sum.
print(add1(3)(4))   # 7


add3 = add1(3)
print(add3(4))  # 7


# Both closures and currying can also return lambda functions
def f(x):
    def g(y):
        return x + y
    return g  # Return a closure.


def h(x):
    return lambda y: x + y  # Return a closure.
