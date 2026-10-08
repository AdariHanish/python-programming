#problem
'''
given a llist of population sensus done by gov we need to find the total population
each element in the list represents total members in a family
'''
l=[4,6,5,8,9,3,2,4,5,4,3,2,3,4]
sum=0
for i in l:
    sum+=i
print("the total population is:",sum)