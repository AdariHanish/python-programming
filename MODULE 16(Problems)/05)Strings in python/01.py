#question
'''
Length of unique words
Problem Description:

Given two sentences, write a program to return the sum of the total number of unique words from each sentence.

Input Format:

The first line indicates the number of test cases.There will be two lines of inputs for each test cases as following:
The two lines consist of two sentences in string format.
Output Format:

The number of unique words from the sentences in integer format.
Sample Input:

1
in data analysis we use data and process it further to create better interpreted data
more and more data will be passively collected
Sample Output:

20
Sample explanation:

{'use', 'process', 'create', 'better', 'analysis', 'in', 'it', 'further', 'and', 'we', 'data', 'interpreted', 'to'} 
represent the 13 unique words from sentence1 and {'collected', 'more', 'be', 'and', 'data', 'passively', 'will'} 
represent the 7 unique words from sentence2. Therefore 13 + 7 = 20 is returned.
Note:

If a word is present in both sentences it should be counted separately for both sentences.
'''
#answer/code
def count_unique_words(sentence):
    words = sentence.split()
    unique_words = set(words)
    return len(unique_words)
t = int(input())
for _ in range(t):
    sentence1 = input().strip()
    sentence2 = input().strip()
    
    count1 = count_unique_words(sentence1)
    count2 = count_unique_words(sentence2)
    
    print(count1 + count2)
