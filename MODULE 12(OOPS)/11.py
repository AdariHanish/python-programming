#method overriding
class Dog:
    def sound(self):
        print("Dog barks: Woof!")
class Cat(Dog):  # Inheriting from Dog
    def sound(self):
        print("Cat meows: Meow!")
# Create objects and call sound method
d = Dog()
c = Cat()
d.sound()  # Calls Dog's method
c.sound()  # Calls Cat's method (overridden)