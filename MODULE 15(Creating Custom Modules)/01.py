#using import
print("---------------using import keyword----------------")
print("this is name function")
import mymod
mymod.name()

#using import
print("\n---------------using import keyword----------------")
print("this is add function")
import mymod
mymod.add(4,5)
#using import
print("\n---------------using import keyword----------------")
print("this is prime function")
import mymod
mymod.prime(7)
#using * ((*) means it imports all the functions and variables)
print("\n---------------using *(All) keyword----------------")
from mymod import *
name()
add(6,6)
prime(8)

#using from
print("\n---------------using from keyword----------------")
from mymod import name
name()

#using as
print("\n---------------using as keyword----------------")
import mymod as m
m.add(2,3)

#import another module
print("\n---------------importing prime module----------------")
from mymod import prime
prime(5)