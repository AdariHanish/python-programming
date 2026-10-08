#polymorphism
class Dog:
    def sound(self):
        print("Dog barks: Woof!")
class Cat:
    def sound(self):
        print("Cat meows: Meow!")
# Polymorphic behavior
def make_sound(animal):
    animal.sound()
# Create objects
d = Dog()
c = Cat()
# Call the same method on different types
make_sound(d)  # Dog's version of sound()
make_sound(c)  # Cat's version of sound()
