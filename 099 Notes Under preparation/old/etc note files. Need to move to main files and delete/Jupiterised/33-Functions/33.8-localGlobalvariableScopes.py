# Local variables
# A variable declared inside the function's body or in the local scope is known as local variable.
def foo1():
    y_local_variable = "local"
foo1()
# print(y_local_variable) # NameError: name 'y_local_variable' is not defined

# The output shows an error, because we are trying to access a local variable y_local_variable in a global scope whereas
# the local variable only works inside foo() or local scope.


# Global variable
# 1 -  A variable declared outside of the function or in global scope is known as global variable. As long as the global
# variable is not manipulated or redeclared/initialised inside the function it can be accessed without the global
# keyword inside the function.
x_global_var = "globalValue"
def foo2():
    print("value inside: ", x_global_var)

foo2()
print("value outside: ", x_global_var)
# value inside:  globalValue
# value outside:  globalValue

# In above code, we created x_global_var as a global variable and defined a foo() to print the global variable
# x_global_var. Finally, we call the foo() which will print the value of x_global_var.

# 2-  Another variable with the same name as global variable can be initialised within the scope of a function. This
#  variable will be treated differently
x = 'I am global'
def foo3():
    x = 'I am local'
    print("local x:", x)
foo3()
print("global x:", x)
# local x: I am local
# global x: I am global

# In above code, we used same name x for both global variable and local variable. We get different result when we print
# same variable because the variable is declared in both scopes, i.e. the local scope inside foo() and global scope
# outside foo().
# When we print the variable inside the foo() it outputs local x: I am local, this is called local scope of variable.
# Similarly, when we print the variable outside the foo(), it outputs global x: I am global, this is called global scope
# of variable.


# 3- What if you want to change value of global 'x_global_var' inside a function?
# https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
# As described above, variables that are only referenced inside a function are implicitly global. If a variable is
# assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
'''
x_global_var = "globalValue"
def foo():
    x_global_var = x_global_var + '2'
    print(x)
foo()
'''
# UnboundLocalError: local variable 'x_global_var' referenced before assignment

# This is because when you make an assignment to a variable 'anywhere' in a scope, that variable becomes local to that
# scope and shadows any similarly named variable in the outer scope.
# The output shows an error because Python treats 'x_global_var' as a local variable and 'x_global_var' is also not
# defined inside foo() therefore --> x_global_var + '2' cannot execute.

# Similarly if we move print(x) to the top, it will still fail at 'print(x_global_var)' as local variables are hoisted
# before function call and the line -> x_global_var2 = '2' which is an assignment has hoisted this variable as a local
# variable in the functions scope.
'''
x_global_var2 = "globalValue"
def foo2():
    print(x_global_var2)
    x_global_var2 = '2'
foo2()
'''
# UnboundLocalError: local variable 'x_global_var2' referenced before assignment

# To make it work, variable either needs to be declared before the print (to be used as a local variable) or be declared
# with the global keyword to use the global one.


