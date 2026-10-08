#printing sum of numbers in given range
print("enter 1 for while loop")
print("enter 2 for for loop")
x=int(input("Enter which loop to choose:"))
if x==1:
    n=int(input("Enter the number:"))
    sum=0
    i=1
    while i<=n:
        sum=sum+i
        i=i+1
    print("sum is:",sum)
elif x==2:
    n=int(input("Enter the number:"))
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("sum is:",sum)
else:
    print("Invalid input")