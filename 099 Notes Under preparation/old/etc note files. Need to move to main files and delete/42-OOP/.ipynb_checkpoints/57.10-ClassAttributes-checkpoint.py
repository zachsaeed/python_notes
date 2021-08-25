#   https://stackoverflow.com/questions/68645/are-static-class-variables-possible-in-python
#   https://stackoverflow.com/questions/44460724/can-i-access-class-variables-using-self
#   https://stackoverflow.com/questions/3434581/accessing-a-class-member-variables-in-python


class User:

    # Class Attribute:
    # - variables declared inside the class definition, but not inside a method are class or
    #   "static" variables:
    # - There will be only one copy of the class attribute regardless how many instances you
    #   create. They live in the class itself and are shared by the class and its instances
    # - We can access the class attribute directly either via <instancename>.<classAttribute>
    #   or <classname>.<classAttribute>
    active_users = 0

    def __init__(self, first, last, age):
        # This is not a class attribute. It is local to the __init__ method only:
        type = 'human'

        # instance attributes:
        self.first = first
        self.last = last
        self.age = age

        # - Following will increment class attribute when an instance is created.
        # - Since it is shared by all instances (there is only one copy),
        #   it will show the number of instances created.
        User.active_users += 1

    # instance methods:
    def logout(self):
        # decrement class attribute when logout is called. Since there is only one copy,
        # it will show the number of instances left after logging out
        User.active_users -= 1  # or type(self).active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

# We can access the same class attribute directly either
# via <instancename>.<classAttribute> or <classname>.<classAttribute>

user_instance1 = User("Joe", "Smith", 68)  # incremented by __init__
# Accessed using <classname>.<classAttribute>
print(User.active_users)  # 1
# Accessed using  <instancename>.<classAttribute>
print(user_instance1.active_users)  # 1

user_instance3 = User("Saquib", "Saeed", 13)  # incremented by __init__
# Accessed using  <instancename>.<classAttribute>
print(user_instance3.active_users)  # 2

# We can access class-attributes inside instance methods
print(user_instance1.logout())  # Joe has logged out
print(User.active_users)  # 2  Accessed using  <classname>.<classAttribute>

# Proof that the  class and all instances share the same class attribute
print(id(User.active_users))
print(id(user_instance1.active_users))
print(id(user_instance3.active_users))
# All the ids are the same

# - Note: We cannot access instance attributes or methods via classname as they only
#   exist in an instance.
# print(User.full_name())  # TypeError: ac_users() missing 1 required positional argument: 'self'
# print(User.first)  # AttributeError: type object 'User' has no attribute



