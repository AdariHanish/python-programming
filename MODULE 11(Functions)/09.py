#default arguments
def add(a=7,b=10):#a has a default value of 7 and b has default value of 10
    return a+b
print("the default sum is:",add())#gives the sum of the default values i.e(7+10)
print("the sum of entered values is:",add(int(input("enter the first number:")),int(input("enter the second number:"))))