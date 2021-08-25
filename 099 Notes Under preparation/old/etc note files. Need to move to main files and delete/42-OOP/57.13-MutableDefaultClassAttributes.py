# https://www.pythonforthelab.com/blog/mutable-and-immutable-attributes-of-classes/
# Classes provide another pattern which is the use of class attributes instead of instance attributes. Class attributes
# are those values that are defined directly in the class, outside of any methods. Let's update our example to use a
# class attribute called var:

class MyClass:
    var = []

    def append(self, value):
        self.var.append(value)

    def __str__(self):
        return str(self.var)

# And we use it as before:
my_class = MyClass()
my_class.append(1)
print(my_class)  # [1]

# If we instantiate the class again, we will have the same as before:
my_class_2 = MyClass()
print(my_class_2)  # [1]

# The main difference with what we have done before is that we can address directly the var attribute of the class:

MyClass.var.append(2)
print(my_class)  # [1, 2]
print(my_class_2)  # [1, 2]

# You can also address the attribute of an instance directly, without the need of the append method:

my_class_2.var += [3]
print(my_class)  # [1, 2, 3]
print(my_class_2)  # [1, 2, 3]

# You can see in the examples above, is that the changes you apply to one of the attributes will be reflected in the
# attributes of all the other instances and even in the class itself. There is a big difference, however, between class
# attributes and default inputs in methods. Class attributes are shared between instances by default even if they are
# immutable. Let's see, for example, what happens if we use a var that is an integer, and therefore immutable:

class MyClass:
    var = 1

    def increase(self):
        self.var += 1

    def __str__(self):
        return str(self.var)

# Just as we have done before, we will instantiate twice the class and see what happens:

my_class = MyClass()
print(my_class)  # 1
my_class_2 = MyClass()
print(my_class_2)  # 1
my_class.increase()
print(my_class)  # 2
print(my_class_2)  # 1

# What you see here is already a big difference. Both instances of MyClass have the same attribute var. However, when
# you increase the value in one of the instances this change is not propagated to the other instance nor to new
# instances of the class.

# This is very different from what you would see if you change the value of var in the class itself:

my_class = MyClass()
my_class_2 = MyClass()
MyClass.var += 1
print(my_class)  # 2
print(my_class_2)  # 2

# You see that class attributes are still linked to the instances. It is very interesting to see the id of the var
# attribute before and after changing its value:
my_class = MyClass()
my_class_2 = MyClass()
print(id(my_class_2.var))  # 10935488
print(id(my_class.var))  # 10935488
print(id(MyClass.var))  # 10935488
MyClass.var += 1
print(id(my_class_2.var))  # 10935520
print(id(my_class.var))  # 10935520
print(id(MyClass.var))  # 10935520

# You see that all the attributes are the same object. When the value is replaced, since integers are immutable, a new
# object is created and is propagated to all the instances of the class. However, if you change the value of var in one
# of the instances, this will not hold anymore:
my_class.var += 1
print(id(my_class.var))  # 10935552
print(id(my_class_2.var))  # 10935520
print(id(MyClass.var))  # 10935520

# You can see that both the attributes in MyClass and in my_class_2 are still the same object, while the identity of var
# in my_class changed. From now on, any changes that you do to MyClass.var are decoupled from the changes in my_class,
# but will still be reflected on my_class_2.

# Keeping in mind the differences between methods' default values and class attributes open a lot of possibilities when
# designing a program. The fact that you can alter all objects from within a specific instance can be of great use when
# properties change at runtime. Even if not an extremely common scenario for short-lived scripts, it is very common when
# dealing with user interaction on programs that run for hours or days.