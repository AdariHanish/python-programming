#question
'''
Members of a Dictionary
What will be the output of the following Python code?

dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}

val = dict1['age']

if val in dict1:
    print('This is a member of the dictionary')
else:
    print('This is not a member of the dictionary')

This is a member of the dictionary
This is not a member of the dictionary
None
Error
'''
#answer/code
#  This is not a member of the dictionary

#check:-
dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}

val = dict1['age']

if val in dict1:
    print('This is a member of the dictionary')
else:
    print('This is not a member of the dictionary')