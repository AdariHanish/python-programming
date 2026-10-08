#question
'''
Triangle Star- Pattern
Problem Description:

Write a function to print the pattern shown in the sample using n given as a parameter, where n defines the number of rows.

Note: There isn't any space between consecutive stars.

Input Format:

The only argument to the function is a number n.
Output Format:

Triangle Star Pattern in string format for each testcase.
Sample Input:

5
Sample Output:

    *
   ***
  *****
 *******
*********
Sample Explanation:

The first row prints n-1 i.e. 4 spaces at the start and then 1 star. 
The second row first prints (n-2=3) spaces and then 3 stars. 
This updating of stars by 2 and spaces by -1 keeps happening until the last row where the space becomes zero.
'''
#answer/code
def triangle_star_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    return '\n'.join(pattern)
n = int(input("Enter number of rows: "))
print(triangle_star_pattern(n))