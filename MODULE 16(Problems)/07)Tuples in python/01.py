#question
'''
Get the index
Problem Description:

Write a function to search for a given element elem in the tuple tup and return its index. Return -1 if elem is not present in tup.

Input Format:

The first line consists of tuple.
The second line consists of an element for which index is required to be returned.
Output Format:

Return the index value in integer format.
Sample Input:

(10, 20, 30, 40, 50)
30
Sample Output:

2
Sample explanation:

30 is present at index 2, therefore 2 is returned.
'''
#answer/code
def get_index(tup, elem):
    if elem in tup:
        return tup.index(elem)
    else:
        return -1
tup = tuple(map(int, input("Enter tuple elements (space-separated): ").split()))
elem = int(input("Enter element to search: "))
print(get_index(tup, elem))