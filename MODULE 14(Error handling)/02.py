#try and except block
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
try:
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")