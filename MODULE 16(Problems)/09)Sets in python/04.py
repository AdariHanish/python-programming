#question
'''
Indexing Sets
Given the names of students in the following set. There was a grammatical mistake in the name "Aurn". It should be 'Arun'. What will be the output if we try to execute the code given below in order to update this name?

a={'Aurn', 'Nikhil', 'Seeta'}
a[0]= 'Arun'
print(a)

{‘Arun’, ‘Nikhil’, ‘Seeta’}
{‘Aurn’, ‘Nikhil’, ‘Seeta’}
{‘Aurn’, ‘Nikhil’, ‘Arun’}
Type Error
'''
#answer/code
#Type Error

#check:-
a={'Aurn', 'Nikhil', 'Seeta'}
a[0]= 'Arun'
print(a)