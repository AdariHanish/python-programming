#2d lists
x = int(input("Enter how many lists are needed in one list: "))
o = []
for i in range(x):
    i = list(map(int, input(f"Enter the ({i + 1}) list elements separated by commas: ").split(",")))
    o.append(i)
print("\nThe 2D list is:", o)
for a in range(len(o)):
    for b in range(len(o[a])):
        print(f"This is {b + 1} element in the {a + 1} list of the 2D list: {o[a][b]}")
