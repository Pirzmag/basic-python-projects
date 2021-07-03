class Dog:
    """a class for dogs!"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def bark(self):
        print(f"{self.name} says 'Woof!'")


class SmallDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f"{self.name} says 'Yapp!'")


Morfi = Dog('Morfi', 4)
Granda = Dog('Granda', 9)
Felek = SmallDog('Felek', 7)

print(f"{Morfi.name} is {Morfi.age} years old. {Granda.name} was {Granda.age}"
      f" years old. {Felek.name} was {Felek.age} years old.")
Granda.bark()
Felek.bark()
Morfi.sit()
