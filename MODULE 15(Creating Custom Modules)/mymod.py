'''
creating a custom module that adds 2 numbers and checks if the numeber is prime or not
this is users own module now he can import it and use it
'''
#name function
def name():
    print("the name is printed by the custom module and the name is:kiran kumari")
    
#addition function
def add(a,b):
    print(f"the addition of two numbers {a} and {b} are:",a+b)
    return a+b

#prime number function
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(f"the number {n} is not prime")
                break
        else:
            print(f"the number {n} is prime")
    else:
        print(f"the number {n} is not prime")
    return n