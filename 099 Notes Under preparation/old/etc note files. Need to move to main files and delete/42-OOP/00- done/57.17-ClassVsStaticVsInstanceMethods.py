# https://www.python-course.eu/python3_class_and_instance_attributes.php

# below, we define a class "Pet" with a method "about". This method should give some general class information. The
# class Cats will be inherited in a subclass "Dog" and "Cat". The method "about" will be inherited as well. We will
# demonstrate that we will meet problems, if we define the method "about" as a normal instance method or as a
# staticmethod. We will start by defining about as an instance method

class Pet:
    _class_info = "pet animals"

    def about(self):
        print("This class is about " + self._class_info + "!")


class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()  # This class is about pet animals!
d = Dog()
d.about()  # This class is about man's best friends!
c = Cat()
c.about()  # This class is about all kinds of cats!

# This may look alright at first at first glance. On second thought we recognize the awful design. We had to create
# instances of the Pet, Dog and Cat classes to be able to ask what the class is about. It would be a lot better, if we
# could just write "Pet.about()", "Dog.about()" and "Cat.about()" to get the previous result. We cannot do this. We will
# have to write "Pet.about(p)", "Dog.about(d)" and "Cat.about(c)" instead.

# Now, we will define the method "about" as a "staticmethod" to show the disadvantage of this approach. As we have
# learned previously in our tutorial, a staticmethod does not have a first parameter with a reference to an object. So
# about will have no parameters at all.Due to this, we are now capable of calling "about" without the necessity of
# passing an instance as a parameter, i.e."Pet.about()", "Dog.about()" and "Cat.about()".Yet, a problem lurks in the
# definition of "about. The only way to access the class info "_class_info" consists in putting a class name in front.
# We arbitrarily put in "Pet". We could have put there "Cat" or "Dog" as well. No matter what we do, the solution will
# not be what we want:

class Pet2:
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("This class is about " + Pet2._class_info + "!")

class Dog2(Pet2):
    _class_info = "man's best friends"

class Cat2(Pet2):
    _class_info = "all kinds of cats"

Pet2.about()  # This class is about pet animals!
Dog2.about()  # This class is about pet animals!
Cat2.about()  # This class is about pet animals!

# This means that we have no way of differenciating between the class Pet and its subclasses Dog and Cat.The problem is
# that the method "about" does not know that it has been called via the Pet, the Dog or the Cat class.

# A classmethod is the solution to all our problems.We will decorate "about" with a classmethod decorator instead of a
# staticmethod decorator:
class Pet3:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")

class Dog3(Pet3):
    _class_info = "man's best friends"


class Cat3(Pet3):
    _class_info = "all kinds of cats"


Pet3.about()  # This class is about pet animals!
Dog3.about()  # This class is about man's best friends!
Cat3.about()  # This class is about all kinds of cats!

# The output is now like we wanted it to be:
