#list slicing
n = list(map(int, input("Enter the list elements separated by commas: ").strip().split(',')))
print("List of integers:", n)
x=int(input(("enter the start index of the list to be sliced:")))
y=int(input(("enter the end index of the list to be sliced:")))
z=int(input(("enter the step size of the list to be sliced:")))
print("Sliced list:", n[x:y:z])