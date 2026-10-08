#scope of the variable
'''
the scope if of 2 types
1)local:-this variable can only be acessed in the particular function or block only
2)global:-this variable can be acessed anywhere in the program
'''
a=int(input("enter the value of a:"))
def add(a,b):
    print("this is the local variable b and its value is:",b)
    return a+b
print("the sum of the local variable b and the global variable a is:",add(a,int(input("enter the value of b:"))))
print("this is the global variable a and its value is:",a)
print("this is local variable b and its value is:",b)#type:ignore #this cant be acessed outside the function as its local variable