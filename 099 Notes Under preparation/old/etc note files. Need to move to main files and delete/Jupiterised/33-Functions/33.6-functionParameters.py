def square(num_param):
    return num_param**2


print(square(4))  # 16
print(square(8))  # 64


def sing_birthday(name):
    print(f"happy birthday {name}")


sing_birthday('saquib')  # happy birthday saquib


# The quantity of parameters can be as many as you want of any types
def print_full_name(first_name, last_name):
    return f'Your fullname is {first_name} {last_name}'


print(print_full_name('Saquib', 'Saeed'))  # Your fullname is Saquib Saeed


# Parameters vs Arguments
# Parameters are the variables in the function definition
# Arguments are the variables which we pass in when the function is called
# / invoked


# Parameters can have default values
# The default values are automatically used if an argument is not specified. When argument id passed,
# it overrides the default values
# default params allows u to be more defensive
# avoid errors with incorrect params
# more readable examples
# default values can be lists, dictionaries, strings, booleans, even other
# functions

def power(num, power=2):
    return num**power


print(power(4))  # 16


# function as default param
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def math(a, b, fn=add):
    return fn(a, b)


print(math(2, 2))  # 4  # default add function used
print(math(5, 2, subtract))  # 3
# The order of params is important. So,
# print(math(subtract, 5, 2))  # Will not work


# Keyword Arguments
# But we can make it work using keyword arguments by assigning arguments to the original name
# of the params in the function definition
print(math(fn=subtract, a=5, b=2)) # 3
# Keyword arguments are useful when passing a dictionary to a function and unpacking its values.


# default params vs keyword arguments
# when you define a function and use =, you are setting a default param but
# when you invoke a function and use =, you are making a keyword argument

