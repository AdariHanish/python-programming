#question
'''
Divide the tuple
Problem Description:

Write a program to divide a given tuple into two tuples that contain even and odd indexed elements of the original tuple. Print both these tuples in the given output format.

Note: The input tuple follows 1-based indexing. This means the element at index 0  is treated as having index as 1. 

For example, (9,2,3). The 1-based index of 2 is 2.

Input Format:

The input contains a tuple as an argument to the function.
Output Format:

Print two tuples one for odd indexed elements and another for even indexed elements in the following format:
Odd: (....)
Even: (....)
Sample Input:

1
(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
Sample Output:

Odd: (10, 5, 10, 10, 5, 8)
Even: (8, 2, 15, 8, 8, 2)
'''
#answer/code
def divide_tuple(tup):
    odd = tuple(tup[i] for i in range(len(tup)) if (i + 1) % 2 == 1)
    even = tuple(tup[i] for i in range(len(tup)) if (i + 1) % 2 == 0)
    print("Odd:", odd)
    print("Even:", even)

# Example usage
tup = (tuple(map(int, input("enter the numbers seperated by comma:").split())))
divide_tuple(tup)