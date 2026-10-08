#lambda function
'''
the lambda function is a small anonymous function that is defined with the lambda keyword.
it can take any number of arguments, but can only have one expression.
syntax:
lambda arguments: expression
'''
#example(general example)
x=lambda a,b:a+b
print("the sum of a and b is:",x(int(input("enter the value of a:")),int(input("enter the value of b:"))))

#example(print in the lambda function itself)
x=lambda a,b:print("the sum of a and b is:",a+b)
x(int(input("enter the value of a:")),int(input("enter the value of b:")))

#example(greater of 2 numbers)
x=lambda a,b:print("a is greater:",a) if a>b else print("b is greater:",b)
x(int(input("enter the value of a:")),int(input("enter the value of b:")))