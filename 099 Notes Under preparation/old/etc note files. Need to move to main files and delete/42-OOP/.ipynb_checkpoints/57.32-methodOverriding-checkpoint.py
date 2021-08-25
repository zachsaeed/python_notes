# 1- Method overriding. This is implemented by having a method in the base (or parent)
# class that is overridden by a method in aa subclass. Example:
#
# Cat.speak()
# Dog.speak()
# Human.speak()


class Animal:
    def speak(self):
        raise NotImplementedError("Subclass neesd to implement this method")


class Cat(Animal):
    # This method overrides the speak() in base class Animal
    def speak(self):
        return "Meow"


class Dog(Animal):
    # This method overrides the speak() in base class Animal
    def speak(self):
        return "Woof"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())  # Woof
f = Fish()
print(f.speak())  # NotImplementedError: Subclass neesd to implement this method

# TODO can we use super to call a super method inside an overloadig method