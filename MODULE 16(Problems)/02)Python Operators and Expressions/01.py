#question
'''
Volume of Sphere in Python
Problem Description:

You are given a positive integer r denoting the radius of a sphere as a parameter. Write a program to calculate the volume of the sphere. The volume of a sphere having radius R is given by (4 * π * R3) / 3.

NOTE: Return the volume of the sphere up to two decimal places. You can use round().

NOTE2: Use pi as 22/7 (not math.pi).

Input Format:

The first line indicates the number of the test cases. For each testcase there will be one line of input:
The one line contains r in integer format.
Output Format:

The volume of the sphere in float format is printed for each testcase in a new line.
Sample Input:

1
8
Sample Output:

2145.52
'''

#answer/code
# Function to calculate the volume of a sphere
def volume_of_sphere(r):
    volume = (4 * 22 * (r ** 3)) / (3 * 7)
    return round(volume, 2)

# Input number of test cases
t = int(input())
for _ in range(t):
    r = int(input())
    print(volume_of_sphere(r))