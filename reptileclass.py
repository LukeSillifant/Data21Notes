from animalclass import Animal

# Reptile inherits from Animal


class Reptile(Animal):

    def __init__(self):
        # Takes from __init__ in Animal
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print("I'll use when threatened!")

    def moving(self):
        print("Move as a reptile.")

# Gives information of what an object represents
    def __repr__(self):
        return f"This is a reptile."

    def __str__(self):
        return f"str version of: This is a reptile."


# Only true when reptileclass is run rather than animalclass
# if __name__ == "animal":

bob = Reptile()
cat = Animal()

bob.breathe()
bob.use_venom()

# Polymorphism: "moving()" used in different ways
cat.moving()
bob.moving()

print(bob)
print(repr(bob))

# Returns __main__ if running module directly, but returns inherited class otherwise
# print(__name__)
