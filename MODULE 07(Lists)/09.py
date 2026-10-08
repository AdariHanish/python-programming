#list compherehension
n = int(input("Enter the number of elements u want in list: "))
x=[i for i in range(1,n+1)]
y=[i*i for i in range(1,n+1)]
z=[i*2 for i in range(1,n+1)]
print("the list is:",x)
print("the square of elements in list is:",y)
print("the element multiplied by 2 is:",z)