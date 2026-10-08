# Hierarchical Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound.")
class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks: Woof!")
class Cat(Animal):  # Cat also inherits from Animal
    def meow(self):
        print("Cat meows: Meow!")
# Create objects
d = Dog()
c = Cat()
# Dog can access sound() and bark()
print("Dog's behavior:")
d.sound()
d.bark()
print("\nCat's behavior:")
# Cat can access sound() and meow()
c.sound()
c.meow()