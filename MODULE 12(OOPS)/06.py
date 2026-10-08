#multilevel inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound.")
class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks: Woof!")
class Cat(Dog):  # Cat inherits from Dog
    def meow(self):
        print("Cat meows: Meow!")
# Create object
c = Cat()
# Call sound method from each
c.sound() #cat is derived from the class dog so it can access the sound method of animal as dog is derived from animal
c.bark()  #cat is derived from the class dog so it can access the bark method of dog
c.meow() #cat can acesses the cat method meow
