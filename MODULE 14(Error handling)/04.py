#finally block in python
a=int(input("enter the first number:"))

b=int(input("enter the second number:"))
try:
    print("the first print is executed")
    print(a/b)
    print("the second print is executed")
except Exception as e:
    print("the error is:",e)
finally:
    print("the finally block is executed")
    