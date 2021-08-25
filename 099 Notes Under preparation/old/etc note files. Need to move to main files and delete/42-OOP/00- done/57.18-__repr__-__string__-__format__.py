# '__repr__(self)',
# To get called by built-int repr() method to return a machine readable representation
# of a type.

# '__str__(self)',
#  Defines behavior for when str() is called on an instance of your class.
# Note: . If we don’t implement __str__() function for a class, then built-in object
# implementation is used that actually calls __repr__() function.

#  The major difference between str() and repr() is intended audience.
#  repr() is intended to produce output that is mostly machine-readable (in many cases,
#  it could be valid Python code even), whereas str() is intended to be human-readable.

# @TODO
# '__format__(self, formatstr)', To get called by built-int string.format() method to return a new style of string.

class User:
    active_users = 0

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

    def __repr__(self):
        return f"{self.first} {self.last} is aged {self.age}"

    def full_name(self):
        return f"{self.first} {self.last}"

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


tom = User('Thomas', 'Jerry', 23)
print(tom)

print(repr(tom))
# Without the __repr__ methd, it prints:   <__main__.User object at 0x014198F0>
# __repr__ is defined here so it will print:   Thomas Jerry is aged 23

print(str(tom))  # Thomas Jerry is aged 23
# INTERVIEW REVISION
# Note: . If we don’t implement __str__() function for a class, then built-in object
# implementation is used that actually calls __repr__() function.

