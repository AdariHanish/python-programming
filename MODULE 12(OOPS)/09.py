#hybrid inheritance
class Animal:
    def speak(self):
        print("Animal speaks.")
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof!")
class Cat(Animal):
    def meow(self):
        print("Cat meows: Meow!")
class Horse(Dog, Cat):  # Multiple inheritance (diamond shape)
    def run(self):
        print("Horse runs fast.")
# Create object of Horse
h = Horse()
# Call all methods
h.speak()   # From Animal 
h.bark()    # From Dog
h.meow()    # From Cat
h.run()     # From Horse
