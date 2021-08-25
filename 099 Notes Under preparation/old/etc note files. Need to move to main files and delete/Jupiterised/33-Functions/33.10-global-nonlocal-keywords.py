# https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
# Global Keyword
# To manipulate global variables within function, we use global keyword to stop it creating a local variable with the
# same name
total = 0
def increment():
    global total  # have to do this fso we can manipulate the global var from inside the function
    total += 1
    return total

# The basic rules for global keyword in Python are:
# - When we create a variable inside a function, it’s local by default.
# - When we define a variable outside of a function, it’s global by default. You don’t have to use global keyword.
# - We use global keyword to read and write a global variable inside a function.
# - Use of global keyword outside a function has no effect

# Global in Nested Functions
# Here is how you can use a global variable in nested function.
def foo():
    x = 20
    def bar():
        global x
        x = 25
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)
foo()
print("x in main : ", x)
# Before calling bar:  20
# Calling bar now
# After calling bar:  20
# x in main :  25

# In the above program, we declare global variable inside the nested function bar(). Inside foo() function, x has no
# effect of global keyword and is treated within the local scope of foo.
# Before and after calling bar(), the variable x takes the value of local variable i.e x = 20.
# Outside of the foo() function, the variable x will take value defined in the bar() function i.e x = 25. This is
# because we have used global keyword in x to create global variable inside the bar() function (local scope).
# If we make any changes inside the bar() function, the changes appears outside the local scope, i.e. foo().
# Also note, global x does not preexist and is created outside the foo function scope

# nonlocal keyword
# Python 3 introduced the nonlocal  keyword that allows you to assign to variables in an outer, but non-global, scope.
#
# Without using nonlocal:
def outside():
    msg = "Outside!"
    def inside():
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)

outside()
# Inside!
# Outside!

# msg  is declared in the outside function and assigned the value “Outside!”. Then, in the inside function, the value
# “Inside!” is assigned to it. When we run outside, msg has the value “Inside!” in the inside function, but retains the
# old value in the outside function.

# We see this behaviour because Python hasn’t actually assigned to the existing msg variable, but has created a new
# variable called msg in the local scope of inside that shadows the name of the variable in the outer scope.

# Preventing that behaviour is where the nonlocal keyword comes in.
def outside():
    msg = "Outside!"
    def inside():
        nonlocal msg
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)
outside()
# Inside!
# Inside!

# Now, by adding nonlocal msg to the top of inside, Python knows that when it sees an assignment to msg, it should
# assign to the variable from the outer scope instead of declaring a new variable that shadows its name.

# The usage of nonlocal is very similar to that of global, except that the former is used for variables in outer
# function scopes and the latter is used for variable in the global scope. Nonlocal variable are used in nested function
# whose local scope is not defined.

# Some confusion might arise about when nonlocal should be used. Take the following function, for instance.
def outside():
    d = {"outside": 1}
    def inside():
        d["inside"] = 2
        print(d)
    inside()
    print(d)

outside()
# {'outside': 1, 'inside': 2}
# {'outside': 1, 'inside': 2}

# It would be reasonable to expect that without using nonlocal the insertion of the “inside”: 2 key-value pair in the
# dictionary would not be reflected in outside. Reasonable, but incorrect, because the dictionary insertion is not an
# assignment, but a method call. In fact, inserting a key-value pair into a dictionary is equivalent to calling the
# __setitem__ method on the dictionary object.

# The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing
# scope. This is important because the default behavior for binding is to search the local namespace first. The
# statement allows encapsulated code to rebind variables outside of the local scope besides the global (module) scope.
#
# Names listed in a nonlocal statement, unlike to those listed in a global statement, must refer to pre-existing
# bindings in an enclosing scope (the scope in which a new binding should be created cannot be determined unambiguously)
#
# Names listed in a nonlocal statement must not collide with pre- existing bindings in the local scope
#
# This means, the variable can be  neither in the local nor the global scope.
