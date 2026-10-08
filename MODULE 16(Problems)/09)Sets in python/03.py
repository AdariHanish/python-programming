#question
'''
Updating Elements
Complete the code snippet with possible statements from options so that the expected output is obtained.

sets = {3, 4, 5} 
___________
print(sets)
Expected Output: {1, 2, 3, 4, 5}

sets.update([1, 2, 3])
sets.add([1, 2 ,3])
sets += [1, 2 ,3]
sets += {1, 2, 3}
sets = sets.union({1, 2, 3})
'''
#answer/code
#sets.update([1, 2, 3])
#sets = sets.union({1, 2, 3})

#check:-
sets = {3, 4, 5} 
sets.update([1, 2, 3])
sets = sets.union({1, 2, 3})
print(sets)