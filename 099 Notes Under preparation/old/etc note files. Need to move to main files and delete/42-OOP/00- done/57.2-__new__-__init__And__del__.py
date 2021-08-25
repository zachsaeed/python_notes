# __new__, __init__ and __del__ are magic methods. Magic methods are predefined
# methods in every python object and are called by python internally. See topic
# on magic methods for details


class Vehicle:
    # The __init__ method is called implicitly by python every time you create an
    # instance of the class
    # It is optional and mainly used to initialise instance attributes so not needed
    # for a class with no attributes and only methods
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f'A new vehicle from {make} has been made')


# To instantiate a class:
car1 = Vehicle('toyota', 'auris', 2008)  # An instance of a new vehicle from toyota has been made

# Note: When we instantiate a class the __new__() magic method is implicitly called
# before the __init__() method. The __new__() method returns a new object (instance),
# which is then initialized by __init__().

print(car1.model)  # auris
car2 = Vehicle('nissan', 'almera', 2004)  # A new vehicle from nissan has been made
car3 = Vehicle('mercedes', 'E-class', '2011')  # A new vehicle from mercedes has been made


# __del__(): Object destructor. Called when an object is garbage collected
# __del__() method will be called only when the garbage collection kicks in. And
# this happens automatically when the reference count of an object becomes zero.



# To see all the instance attributes and magic methods, use
print(dir(car3))
# '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'make', 'model', 'year']
