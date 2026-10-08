#multiple inheritance
# Parent class 1
class Dog:
    def bark(self):
        print("Dog barks: Woof!")

# Parent class 2
class Cat:
    def meow(self):
        print("Cat meows: Meow!")

# Child class inheriting from both Dog and Cat
class Animal(Dog, Cat):
    def sound(self):
        print("Animal can bark and meow.")

# Create an object of Animal
a = Animal()
a.sound()
a.bark()
a.meow()
#the animal can acesses all the methods as the animal is inheriting from both the parent classes