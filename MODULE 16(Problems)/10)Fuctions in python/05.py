#question
'''
Calculate Interest
Considering the Interest() function:

def Interest(p,c,t=2,r=0.09):
  return p*t*r
Which of the following function calls are legal?

Interest(p=1000,c=5)
Interest(r=0.05,5000,3)
Interest(500,t=2,r=0.05)
Interest(c=4,r=0.12,p=5000)
'''
#answer/code
# Interest(p=1000,c=5)
# Interest(c=4,r=0.12,p=5000)

#check:-
def Interest(p,c,t=2,r=0.09):
  return p*t*r
Interest(p=1000,c=5)
Interest(c=4,r=0.12,p=5000)