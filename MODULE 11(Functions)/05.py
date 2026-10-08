#returning multiple values from a function
def all(a,b):
    #the values should be stored for getting to the return function
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print("this is addition:",c)
    print("this is subraction:",d)
    print("this is multiplication:",e)
    print("this is division:",f)
    return c,d,e,f
x=all(10,20)
print("this is defalut function call:",x)
print(type(x))
print("---------------this is user defined values---------------------")
print(all(int(input("enter the first number:")),int(input("enter the second number:"))))
print(type(x))