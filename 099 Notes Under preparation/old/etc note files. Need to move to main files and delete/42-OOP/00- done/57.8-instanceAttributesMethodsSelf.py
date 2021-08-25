# A User class with both instance attributes and instance methods
class User:

    def __init__(self, first, last, age):
        # instance attributes are always defined here with self.<attribute name>
        self.first = first
        self.last = last
        self.age = age

    # instance methods always have the first parameter as 'self' or any
    # other name which points to the instance itself. Note: It can be any name
    # other than self too as python will automatically pass self to the first most
    # param when the function is invoked via instance of this class
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

    # if we have an instance method without a self param, it will throw an
    # error as python will try to pass self argument to it while the function
    # definition doesnt define any parameters. See invocation in end below:
    def say_hi():
        print('Hello')

# when instance methods are called after instantiation, the self argument is
# automatically passed in by python, and doesnt need to be passed in explicitly


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user2.initials())
print(user1.initials())

print(user2.is_senior())
print(user1.age)  # Print age before we update it
print(user1.birthday())  # updates age
print(user1.age)  # Print new value of age

# user1.say_hi()  # Error: TypeError: say_hi() takes 0 positional
# arguments but 1 was given
