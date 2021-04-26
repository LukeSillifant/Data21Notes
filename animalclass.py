class Animal:

    def __init__(self):
        self.Alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and out.")

    def eat(self):
        print("Nom nom nom.")

    def moving(self):
        print("Forwards, backwards and side to side.")


if __name__ == "animal":

    cat = Animal()
    cat.breathe()

    print(__name__)