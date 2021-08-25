# - Inheritance Example Using Super()
# - super() refers to the parent or base class of the current class it is called in
# - super() doesnt have to be the first thing to call in constructor. Sometimes you
#   need to validate the arguments before calling super(). So in short you should be
#   able to call it anywhere.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        # self.name = name
        # self.species = species
        # The above is code duplication as it already exists in super class hence we can call:
        # Animal.__init__(self, name, species="Cat")
        # or much better/shorter way using super (Dont have to specify self):
        super().__init__(name, species="Cat")  # Super refers to Animal. Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")
blue.play()


# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy
