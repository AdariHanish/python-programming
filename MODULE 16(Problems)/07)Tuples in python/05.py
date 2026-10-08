#question
'''
Access Tuples
What is the output of the following:

elements = (10, 20, 30, 40, 50, 60, 70, 80)
print(elements[2:5], elements[:4], elements[3:100])

(30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)
(30, 40, 50) (10, 20, 30, 40) (30, 40, 50, 60, 70, 80)
(30, 40, 50, 10, 20, 30, 40, 40, 50, 60, 70, 80)
Error
'''
#answer/code
# (30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)

#check:-
elements = (10, 20, 30, 40, 50, 60, 70, 80)
print(elements[2:5], elements[:4], elements[3:100])