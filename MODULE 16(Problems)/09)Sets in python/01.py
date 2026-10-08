#question
'''
Frequency of unique elements
Problem Description:

Write a function to print out the frequency of all the unique elements present in a given tuple.

Input Format:

The one input line consists of a tuple.
Output Format:

Unique elements and their frequencies are expected to be printed as follows:  
unique_element1 : freq1  
unique_element2 : freq2  
.  
.
Sample Input 1:

(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
Sample Output 1:

10 : 3
8 : 4
5 : 2
2 : 2
15 : 1  
Sample Input 2:

(100, -10, -10, “ONE”, [22], [22], “ONE”)
Sample Output 2:

100 : 1
-10 : 2
ONE : 2
[22] : 2
'''
#answer/code
from collections import defaultdict

def frequency_of_unique_elements(tup):
    freq = defaultdict(int)
    
    for item in tup:
        key = str(item) if isinstance(item, (list, dict, set)) else item
        freq[key] += 1

    for k, v in freq.items():
        print(f"{k} : {v}")

# Example usage
# Sample Input 1
tup1 = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
frequency_of_unique_elements(tup1)

print("\n---\n")

# Sample Input 2 (manually creating mixed types)
tup2 = (100, -10, -10, "ONE", [22], [22], "ONE")
frequency_of_unique_elements(tup2)