#problem
'''
finding the unique words in a sentence
'''
s=input("enter the sentence:")
s=s.title()
s=s.split()
s=set(s)
print("the unique words of the sentence is:",s)