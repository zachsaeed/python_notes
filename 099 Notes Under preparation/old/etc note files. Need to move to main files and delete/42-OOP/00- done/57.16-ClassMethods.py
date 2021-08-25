# - Class methods are methods (with the @classmethod decorator) that are not concerned with the instances, but the class
#   itself.
# - All class methods take the reference to class-object as a first default parameter (just like instance methods take
#   reference to instance-object as a first parameter). P.S. Python classes are instances and therefore objects
#   themselves.
# - We cannot access 'self' (ref to instance-object) inside a class method as self-reference only comes into existence
#   after instantiation. Therefore class methods can access only class attributes but not instance attributes.
# - There will be only one copy of the class method regardless how many instances you create. They live in the class
#   itself and are shared by the class and its instances. Therefore, can be accessed as:
#   <classname>.classmethod or <instancename>.classmethod
# - Class methods are used when the method does not need to know bout the specific instance. Instance methods are the
#   opposite.


class User:
    active_users = 0  # class attribute

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


tom = User.from_string("Tom,Jones,89")
# instance methods:
print(tom.first)  # Tom
print(tom.full_name())  # Tom Jones
print(tom.birthday())  # Happy 90th, Tom

# class method. Accessible using both instance and class
print(tom.display_active_users())  # There are currently 1 active users
print(User.display_active_users())  # There are currently 1 active users

# INTERVIEW REVISION
# - Uses:
#  - One use people have found for class methods is to create inheritable alternative constructors.
# - Python doesn't allow constructor/method overloading so we cannot create more than one __init__()s accepting
#   different params. Therefore, we use class method to create factory methods.
# - Factory methods return class object ( similar to a constructor) for different use cases.
# - It is an alternative way to create objects ie, when we need to accept parameters to the class constructor but the
#   parameters are not compatible with constructor.
# - For example:

# - We can create dictionary using the constructor (__init__()):
my_dictionary1 = dict(name='Saquib', address='chadwell heath', pet='cat')
# {'name': 'Saquib', 'address': 'chadwell heath', 'pet': 'cat'}
print(my_dictionary1)

# - or we can call a class method in the dict class which will process a different structure of params and still return
#   a dic object:
my_dictionary2 = dict.fromkeys(['name', 'address', 'pet'], 'unknown')
# {'name': 'unknown', 'address': 'unknown', 'pet': 'unknown'}
print(my_dictionary2)
# fromkeys() restructures the params and then still calls the __init__()

# They are often also used, where we have static methods, which have to call other static methods. In static methods,
# we have to hard code the class name to access it's attributes. This is a problem, if we are in a use case, where we
# have inherited classes. Therefore, we use class methods instead.
