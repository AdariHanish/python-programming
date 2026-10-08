#return list with unique numbers:
#complex method
'''
in this method a new empty list is created and then from the old list
it will take the elements and checks everytime wether the element is in new list or not
if element is not in new list then it is added to new list
else it wil discard
'''
print("------------------this is normal method which is complex---------------------")
def unique_list(list):
    unique_list = []
    for num in list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
unique_list(list(map(int(input("enter the numbers seperated by comma:").split(",")))))

#simple method
'''
in this method the list is converted into set and then set is converted back to list
as the set dosent allow the duplicate elements all the duplicate elements are removed
and the unique elements are remained in the list
'''
print("------------------this is simple method---------------------")
def unique_list(list):
    return list(set(list))
unique_list(list(map(int(input("enter the numbers seperated by comma:").split(",")))))