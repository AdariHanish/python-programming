#question
'''
Changing Attributes
Consider the following dictionary:

freshers = {
    'student1': {'name': 'yash', 'salary': 7500},
    'student2': {'name': 'heet', 'salary': 8000},
    'student3': {'name':'smit', 'salary': 6500}
}
Which of the following is the correct way of changing the ‘salary’ of ‘smit’ to 8500?

freshers['smit']['salary'] = 8500
freshers['student3']['name' == 'smit']['salary'] = 8500
freshers['student3']['salary'] = 8500
freshers['student3']['salary' == 6500] = 8500
'''
#answer/code
# freshers['student3']['salary'] = 8500

#check:-
freshers = {
    'student1': {'name': 'yash', 'salary': 7500},
    'student2': {'name': 'heet', 'salary': 8000},
    'student3': {'name':'smit', 'salary': 6500}
}
freshers['student3']['salary'] = 8500
print(freshers)