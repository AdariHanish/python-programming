#print even numbers
def even(*args):
    for i in args:
        if i%2==0:
            print(i)
even(*set(map(int,input("enter the numbers seperated by commas:").split(","))))