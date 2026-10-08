#default followed by non default
'''
def add(a=7,b=10,c):
    print(a+b+c)
add(30)
this code is returns the error because c is followed by the default values and is not given a default value
'''
'''
note:-
every time the non default arguments/parameters should be given first 
after the non default are given then only the default arguments/parameters can be given
if no we will get errors
'''
def add(a,b=10,c=110):
    print(a+b+c)
add(int(input("enter the value of a:")))