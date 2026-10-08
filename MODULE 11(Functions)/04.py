#return function
'''
the return function will send the output of the function to the place where it is called
'''
#not using return function
print("--------------------without using return function------------------")
def add(a,b):
    print(a+b)
x=add(10,20)
print("this is predefined add:",x)#this give none in the output as the x is not returning any value
print("--------------this is user defined add-------------")
print(add(int(input("enter the first number:")),int(input("enter the second number:"))))
print(type(x))#this will also give the nonetype as the x is not returning any value
print("\n")

#using return function
print("--------------using the return function-------------")
def add(a,b):
    return a+b
x=add(10,20)
print("this is predefined add:",x)
print("--------------this is user defined add-------------")
print(add(int(input("enter the first number:")),int(input("enter the second number:"))))
print(type(x))
