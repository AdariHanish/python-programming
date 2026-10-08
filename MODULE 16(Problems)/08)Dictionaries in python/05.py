#question
'''
Update Dictionaries
What will be the output of the following Python code snippet?

bbt = {'Sheldon': 1, 'Leonard': 2}
bbt.update({'Penny': 2})
print(bbt)

{“Sheldon”: 1, “Leonard”: 2}
{“Sheldon”: 1, “Penny”: 2}
{“Sheldon”: 1, “Leonard”: 2, “Penny”: 2}
Error
'''
#answer/code
# {“Sheldon”: 1, “Leonard”: 2, “Penny”: 2}
#check:-
bbt = {'Sheldon': 1, 'Leonard': 2}
bbt.update({'Penny': 2})
print(bbt)