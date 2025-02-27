class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

    def make_sound(self):
        pass  # To be implemented in child classes

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cow", age)

    def make_sound(self):
        print(f"{self.name} moos!")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Chicken", age)

    def make_sound(self):
        print(f"{self.name} clucks!")

    def lay_egg(self):
        print(f"{self.name} laid an egg.")

class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Horse", age)

    def make_sound(self):
        print(f"{self.name} neighs!")

    def run(self):
        print(f"{self.name} is running fast!")

# Creating instances
cow = Cow("Bessie", 5)
chicken = Chicken("Clucky", 2)
horse = Horse("Thunder", 4)

# Calling methods
cow.eat()
cow.make_sound()
cow.produce_milk()
print()

chicken.eat()
chicken.make_sound()
chicken.lay_egg()
print()

horse.eat()
horse.make_sound()
horse.run()