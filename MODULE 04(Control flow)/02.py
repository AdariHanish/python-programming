#nested if-else
a=int(input("enter the value of a:"))
if a>0:
    print("a is positive")
    if a%2==0:
        print("a is even")
    else:
        print("a is odd")
else:
    print("a is negative")