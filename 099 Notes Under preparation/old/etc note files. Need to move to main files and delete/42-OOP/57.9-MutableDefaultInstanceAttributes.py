# https://www.pythonforthelab.com/blog/mutable-and-immutable-attributes-of-classes/
# Default values for attributes can be defined in different ways in your classes. Let's start by looking at what happens
# if you define them in the __init__ method. Let's start with a simple class that takes one list as the argument when
# instantiating:

class MyClass:
    def __init__(self, var=[]):
        self.var = var

    def append(self, value):
        self.var.append(value)

    def __str__(self):
        return str(self.var)

# This is a very simple example that already will show a very peculiar behavior. The __init__ takes one list as the
# argument, and if it is not provided it will use an empty list as default. We have also added a method for appending
# values to the list. The __str__ method was defined for convenience to explore the contents of the var attribute. We
# can instantiate the class and use it as always:
my_class = MyClass()
print(my_class)  # []
my_class.append(1)
print(my_class)  # [1]

# So far so good, but let's see what happens when we instantiate the second class:
my_class_2 = MyClass()
print(my_class_2)  # [1]

# The second time you instantiate a class, it will use a different default value! It is actually using the updated value
# from the first instance. Moreover, if you change the value of the second instance, the value of the first instance
# will also change:
my_class_2.append(2)
print(my_class)  # [1, 2]

# Whatever changes you do to the attribute var of one of the objects, will be reflected into the other. Both attributes
# are actually the same object, as you can verify by looking at their ids:
print(id(my_class.var))  # 140228152031752
print(id(my_class_2.var))  # 140228152031752
# But the two instances are different
print(id(my_class))  # 140228175513360
print(id(my_class_2))  # 140228175513304

# The same pattern that appeared while using mutable variables as defaults with functions will appear when using mutable
# default arguments of methods in custom classes. If you want to avoid this from happening, you can always check what we
# have done when working with functions. (See 33.26 and 33.28)

# Of course, the same pattern will appear if you use a mutable variable defined outside of the class, for example:
my_list = [1, 2, 3]
my_class = MyClass(my_list)
my_class.append(4)
print(my_list) # [1, 2, 3, 4]
