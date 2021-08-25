# INTERVIEW REVISION
# it is not a python exclusive feature, since almost every dynamic language presents that behavior.
# Quite simply put, Duck typing gives a programmer the ability to not worry about the type of a class rather perform
# the required operations.
# The canonical example (and the reason behind the name) is the duck test:
# If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

# Example:
class Duck:
    def quack(self):
        print("Quacked")

class AnotherDuck:
    def quack(self):
        print("Louder Quack")

class Eagle:
    def fly(self):
        print("Dude i just fly")

class MakeItQuack:
    def __init__(self, bird):
        bird.quack()

MakeItQuack(Duck())
MakeItQuack(AnotherDuck())
MakeItQuack(Eagle())

# If we execute this code:

# Quacked
# Louder Quack
# Traceback (most recent call last):
#   File "/Users/gaurav/personal/development/grasp-python/base/advanced/duck_typing.py", line 33, in <module>
#     MakeItQuack(Eagle())
#   File "/Users/gaurav/personal/development/grasp-python/base/advanced/duck_typing.py", line 29, in __init__
#     bird.quack()
# AttributeError: 'Eagle' object has no attribute 'quack'

# Observe here we are passing an object bird to MakeItQuack class constructor and invoking quack() on the passed object.
# Thus classes which have an implementation of quack method will be able to call (Duck, AnotherDuck objects) whereas we
# get a AttributeError if we try to pass an object which does not provide an implementation of quack() here the Eagle
# class.

# Also, this is a classical example of dependency injection. My class MakeItQuack receives an instance of a bird and
# uses it in the __init__ method, where it calls the quack method. Note that MakeItQuack does not depends on any
# concrete implementation of bird. And I'm not importing any other type! Just using a dependency injected instance of
# something that responds to a quack message. I could say my class makeItQuack depends on an interface. But I did not
# have to declare it. It is an automatic interface!

# My class MakeItQuack depends on an interface. I don't need to explicit implement the interface. It's already
# implemented if I define the method quack.

# This is the essence of duck typing. Having the ability to do this without writing an Interface is really awesome.

# In a language without dynamic typing, Duck and AnotherDuck would belong to an interface with quack method.
# The bird variable would be of that interface type, and wont accept an Eagle instance as its a different type.
