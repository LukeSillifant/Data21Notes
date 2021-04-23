class AmazingDog:

    # Initialisation
    def __init__(self, animal_kind):
        self.animal_kind = animal_kind
        self.bark()
        self.__is_alive = True

    def bark(self):
        return "woof!"

    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status

    def get_is_alive(self):
        return self.__is_alive


# Instance of a class
Bob = AmazingDog("canine")
Sue = AmazingDog("dolphin")


print(Bob.animal_kind)
print(Sue.animal_kind)

# Produces error
# print(Bob.__is_alive)
print(Bob.get_is_alive())
