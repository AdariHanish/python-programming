#question
'''
Cricket Players
Which of the options adds the elements 'Dhoni' and 'Virat' to the end of the given list?

players = ['Jadeja','Rahul','Rohit'].

So, the resultant list will be players = ['Jadeja','Rahul','Rohit','Dhoni','Virat'].

 

players+='Dhoni Virat'
players[len(players):] = ['Dhoni', 'Virat']
players[-1:] = ['Dhoni', 'Virat']
players+=['Dhoni', 'Virat']
'''
#answer/code
# players[len(players):] = ['Dhoni', 'Virat']
# players+=['Dhoni', 'Virat']

#check:-
players = ['Jadeja','Rahul','Rohit']
players[len(players):] = ['Dhoni', 'Virat']
players+=['Dhoni', 'Virat']
print(players)