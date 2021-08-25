# As per pep8 convention, class names need to be camel case
# while attribute and method names need to be snake case

# A class is a simple blueprint/template for our object/instance. It is a collection
# of attributes and methods which will be created when we instantiate the class

# Simplest class format:
class User:
    pass  # use pass as empty classes not allowed and throw errors

# We can also do:
class ClassName(object):
    pass
# In Python 3, there is no difference, since all classes implicitly
# inherit from object


# Create an instance/object of the above class (from the blueprint)
user1 = User()

print(user1)  # <__main__.User object at 0x03420E90>
print(type(user1))  # <class '__main__.User'>

# we can create as many user objects as we want



