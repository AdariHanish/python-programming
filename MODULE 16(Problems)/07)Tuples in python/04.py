#question
'''
Adding to a tuple
Predict the output of the following code as we are trying to append to an immutable tuple:

name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)

(“Item_1”, 0.5, name_lst)
(“Item_1”, 0.5, [“Vijay”, “Vickey”])
(“Item_1”, 0.5, [“Vijay”, “Vickey”, “Vishal”])
Error
'''
#answer/code
#(“Item_1”, 0.5, [“Vijay”, “Vickey”, “Vishal”])

#check:-
name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)