#Diamond pattern
n=int(input("Enter the number:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))   #upper triangle
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))   #lower triangle
    