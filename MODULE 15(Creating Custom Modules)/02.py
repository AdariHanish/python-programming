'''
in python we have the sympy module which has a function called isprime which checks if a number is prime or not
so that we dont need to write the prime number function again and again
we can directly import the isprime function from the sympy module and use it
'''
from sympy import isprime
num=int(input("enter a number:"))
print(isprime(num))