#question
'''
Similar Substrings
Problem Description

You are given two strings, A and B. Two strings, X and Y, are said to be similar if :

Length(X) = Length(Y).
The frequency of each character in string X should be equal to that of each character in string Y.

String B consists of only lowercase Latin characters, and String A consists of lowercase Latin letters and characters “?”. You can replace the “?” character with any lowercase Latin letter.

Find the number of substrings of string A similar to string B.

For ex: “a?b?c” is similar to “aabcc”, “bcabb”, etc.


Problem Constraints

1 ≤ |A| ≤ 105
1 ≤ |B| ≤ 105


Input Format

The first argument given is a string, A.

The second argument given is a string, B.



Output Format

Return an integer denoting the number of substrings of string A that are similar to string B.



Example Input

Input 1:




 A = "bb??x???"      B = "aab"


Input 2:

 A = "ab?c"          B = "acb"








Example Output

Output 1:




 2


Output 2:

 2







Example Explanation

Explanation 1:




We can find two similar substrings in A:
1) "b??": we can replace both the "?" with "a", to form "baa" which is similar to "aab".
2) "???": we can replace it with "aab".


Explanation 2:

We can find two similar substrings in A:
1) "ab?": we can replace the "?" with "c", to form "abc" which is similar to "acb".
2) "b?c": we can replace the "?" with "a", to form "bac" which is similar to "acb".
'''
#answer/code
from collections import Counter

def similar_substrings(A, B):
    lenA, lenB = len(A), len(B)
    if lenA < lenB:
        return 0

    b_freq = Counter(B)  # Frequency map of B
    window_freq = Counter(A[:lenB])  # Initial window
    count = 0

    def is_similar(window, b_freq):
        wildcard = window.get('?', 0)
        total_missing = 0
        for char in b_freq:
            total_missing += max(0, b_freq[char] - window.get(char, 0))
        return total_missing <= wildcard

    if is_similar(window_freq, b_freq):
        count += 1

    # Slide the window across A
    for i in range(lenB, lenA):
        # Remove the char going out of the window
        out_char = A[i - lenB]
        window_freq[out_char] -= 1
        if window_freq[out_char] == 0:
            del window_freq[out_char]

        # Add the new char
        in_char = A[i]
        window_freq[in_char] += 1

        # Check similarity again
        if is_similar(window_freq, b_freq):
            count += 1

    return count
A = input().strip()
B = input().strip()
print(similar_substrings(A, B))
