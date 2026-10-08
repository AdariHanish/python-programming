#question
'''
Handle division by zero
'''
#answer/code
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")