#question
'''
String Concatenation I
Problem Description

You have 2 strings (A and B).

You have to concatenate two strings and return the concatenated string.



Problem Constraints
1 <= A.size() <= 1000

1 <= B.size() <= 1000



Input Format
First argument containing a lowercase string A.

Second argument containing a lowercase string B.



Output Format
You have to return concatenated string.



Example Input
Input 1:

A = "interview", B = "bit"


Example Output
Output 1:

interviewbit


Example Explanation
Explanation 1:

Clearly, interview bit = interviewbit.
'''
#answer/code
def concatenate_strings(A, B):
    return A + B

# Sample usage:
A = input("Enter first string: ")
B = input("Enter second string: ")
print(concatenate_strings(A, B))