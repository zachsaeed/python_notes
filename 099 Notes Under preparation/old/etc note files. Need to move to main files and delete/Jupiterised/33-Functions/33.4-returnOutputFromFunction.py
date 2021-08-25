# we return output using the return keyword
def square_of_seven():
    return 7**2


result = square_of_seven()
print(result)  # 49

# Note: when return is called,
# It exits the function
# Outputs whatever value is placed after the return keyword
# pops the function of the call stack


def square_of_eight():
    print('Before the return')
    return 8**2
    # because o the return before this line, code will
    print('After the return')
    # end execution and never reach this point


result = square_of_eight()  # prints: Before the return
print(result)  # 64

# Common mistakes with return
# 1- be very careful with position of return. eg if its places inside a for loop it will break the
# function as the first loop is run
# 2- if <condition>:
#       return True
#    else
#       return False
# in the above example 'else' is not really required and can be written as
#    if <condition>:
#       return True
#    return False


# Returning multiple values
# In Python, we can return multiple values from a function. Following are the different 4 ways

# 1) Using Object: This is similar to C / C + + and Java, we can create a class(in C, struct) to hold multiple values
#   and return an object of the class.
class Test:
    def __init__(self):
        self.str_value = "geeksforgeeks"
        self.x = 20

# This function returns an object of Test
def fun():
    return Test()

t = fun()
print(t.str_value)  # geeksforgeeks
print(t.x)  # 20

# Below are some more interesting methods for somebody shifting C++ / Java world.


# 2) Using Tuple:
#   A Tuple is a comma separated sequence of items.It is created with or without (). Tuples are immutable.

def fun():
    str_value = "geeksforgeeks"
    x = 20
    return str_value, x;  # Return tuple, we can also write (str_value, x)


str_value, x = fun()  # Assign returned tuple
print(str_value)  # geeksforgeeks
print(x)  # 20


# 3) Using a list: A list is like an array of items created using square brackets.They are different from arrays as
# they can contain items of different types.Lists are different from tuples as they are mutable.
def fun():
    str_value = "geeksforgeeks"
    x = 20
    return [str_value, x];

list = fun()
print(list)  # ['geeksforgeeks', 20]


# 4) Using a Dictionary: A Dictionary is similar to hash or map in other languages.
def fun():
    d = dict();
    d['str_value'] = "GeeksforGeeks"
    d['x'] = 20
    return d


# Driver code to test above method
d = fun()
print(d)  # {'x': 20, 'str_value': 'GeeksforGeeks'}
