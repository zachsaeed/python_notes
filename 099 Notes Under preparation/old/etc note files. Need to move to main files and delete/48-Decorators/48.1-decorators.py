# Decorator is a pattern
# Decorators are actually higher order functions that use closure
# wrap other functions and enhance/change their behaviour
# Are higher order functions (They accept other function and return function)
# Have their own syntax using "@" (syntactic sugar)

# Syntax:


def be_polite(fn):  # higher order function as it accepts and returns a function
    def wrapper():  # nested function
        print("What a pleasure to meet you!")
        fn()  # closure
        print("Have a great day!")
    return wrapper  # return the nested function


@be_polite
def greet():
    print("My name is Colt.")
# What a pleasure to meet you!
# My name is Colt.
# Have a great day!


@be_polite
def rage():
    print("I HATE YOU!")
# What a pleasure to meet you!
# I HATE YOU!
# Have a great day!

greet()
rage()


# What actually happening is:
def be_polite_decorator(fn):  # higher order function as it accepts and returns a function
    def wrapper():  # nested function
        print("What a pleasure to meet you!")
        fn()  # closure
        print("Have a great day!")
    return wrapper  # return the nested function


def greet2():
    print("My name is Colt.")


def rage2():
    print("I HATE YOU!")


# we are decorating our function with politeness!
greet_decorated = be_polite_decorator(greet2)
polite_rage_decorated = be_polite_decorator(rage2)

# call the decorated functions:
greet_decorated()
# What a pleasure to meet you!
# My name is Colt.
# Have a great day!

polite_rage_decorated()
# What a pleasure to meet you!
# I HATE YOU!
# Have a great day!

# The problem here is that our decorator doest work with arguments. Resolved in next file
