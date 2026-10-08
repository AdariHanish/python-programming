#except block
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
try:
    print(a/b)
except Exception as e:
    print("error is:",e)
