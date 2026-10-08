#question
'''
Find the Area of Circle
Problem Description:

Write a function to calculate and return the area of a circle by using the radius of the circle given as a parameter.

Notes:

 Round up the area to 2 decimal places. You can use the round() function.
 Use pi as 3.14159.
 You need not take input in this problem, you need to only implement the function provided.
Input Format:

The first line indicates the number of the test cases. 
For each test case there will be one line of input in integer format representing radius.
Output Format:

Area in float format rounded upto 2 decimal places for each testcase.
Sample Input:

1  
5
Sample Output:

78.54
 

Sample explanation:

The area for circle with radius 5cm is 3.14159 x (5 x 5) = 78.53975 cm2

After rounding by 2 digits, it becomes 78.54 cm2
'''
#answer/code
def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return round(area, 2)

# Read number of test cases
T = int(input())
for _ in range(T):
    r = int(input())
    print(area_of_circle(r))