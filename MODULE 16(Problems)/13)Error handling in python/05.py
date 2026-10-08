#question
'''
Custom exception
'''
#answer/code
class MyError(Exception):
    pass

try:
    raise MyError("Something custom went wrong!")
except MyError as e:
    print(e)