#function level polymorphism
#len
print(len("hello"))        # String → returns number of characters
print(len([1, 2, 3, 4]))    # List → returns number of elements
print(len((10, 20, 30)))   # Tuple → returns number of items
'''print(len(234)) o/p:-#gives error as the len function is not defined for integer'''
#sum
print(sum([1, 2, 3]))       # List → sum of numbers
print(sum((4, 5, 6)))       # Tuple → sum of numbers
'''print(sum(453)) o/p:-#gives error as the sum function is not defined for integer'''
#custom
def mul(*args):
    total=1
    for i in args:
        total=total*i
    return total
mul(*tuple(map(int,input("enter the numbers seperated by comma: ").split(","))))