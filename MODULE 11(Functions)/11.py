#arbitary arguments
def add(*args):
    sum=0
    print("the numbers are:",args)
    print("the datatype of args is:",type(args))
    for i in args:
        sum+=i
    print("the sum of the numbers is:",sum)
    return sum
a=add(*set(map(int,input("enter the numbers seperated by commas:").split(","))))
print("the datatype of the sum of numbers is:",type(a))
'''
here in the statement:add(*tuple(map(int,input("enter the numbers seperated by commas:").split(","))))
we use the * operator before the tuple keyword to unpack the tuple 
then the tuple is unpacked into individual arguments for passing the values to add() function.
without the * it gives the error
'''