# https://micropyramid.com/blog/python-special-class-methods-or-magic-methods/
# 2- Operator overriding where the same operation works differently for different kinds of
# objects (Internally via special dunder methods).
# https://docs.pytho n.org/3/reference/datamodel.html#special-method-names
#
# print(2 + 2)  # 4
# print('2'+'2')  # '22'
# - + works differently with different types of objects. This is achieved by special methods
#   (also known as "magic methods") defined in classes and are __dunders__().
# - These methods give instructions to python for how to deal with objects for example how 2
#   objects should be added etc.
# - The + operator i shorthand for a special method called __add__() that gets called on
#   the first operand
# - If the first (left) operand is an instance of int, __add__() does mathematical
#   addition. If it's a string, it does string concatenation

from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    # Similarly, we can declare special methods in our on classes to mimic the behaviour
    # of built-in objects, like __len__ object
    def __len__(self):
        return self.age
   # If we do not define len, TypeError: object of type 'Human' has no len()

    def __add__(self, other):
        # When you add two humans together...you get a newborn baby Human!
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        # When you multiply a Human by an int, you get clones of that Human!
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "CANT MULTIPLY!"


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# executes __repr__
print(j)  # Human named Jenny Larsen aged 47
print(len(j))  # 47  # If we do not define __len__ in class above,  TypeError: object of type 'Human' has no len()
triplets = j * 3
print(triplets)  # [Human named Jenny Larsen aged 47, Human named Jenny Larsen aged 47, Human named Jenny Larsen aged 47]
triplets = (k + j) * 3
print(triplets)  # [Human named Newborn Jones aged 0, Human named Newborn Jones aged 0, Human named Newborn Jones aged 0]
