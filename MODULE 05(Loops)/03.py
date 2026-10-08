# printing even numbers in given range using while loop
print("enter 1 for while loop")
print("enter 2 for for loop")
x=int(input("Enter which loop to choose:"))
if(x==1):
    print("------------this is while loop--------------")
    n=int(input("Enter the number:"))
    i=0
    while i<=n:
        if i%2==0:
            print(i)
        i=i+1
elif x==2:
    print("------------this is for loop--------------")
    n=int(input("Enter the number:"))
    for i in range(0,n+1):
        if i%2==0:
            print(i)
else:
    print("Invalid input")