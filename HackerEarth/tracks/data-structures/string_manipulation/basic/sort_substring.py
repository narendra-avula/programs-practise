__author__ = 'Naidu'
'''
Sort the Substring
Given a string
S
S, and two numbers
N
N,
M
M - arrange the characters of string in between the indexes
N
N and
M
M (both inclusive) in descending order. (Indexing starts from 0).

Input Format:
First line contains
T
T - number of test cases.
Next T lines contains a string(
S
S) and two numbers(
N
N,
M
M) separated by spaces.

Output Format:
Print the modified string for each test case in new line.

Constraints:

1
?
T
?
1000
1?T?1000
1
?
|
S
|
?
10000
1?|S|?10000 // |S| denotes the length of string.
0
?
N
?
M
<
|
S
|
0?N?M<|S|
S
?
[
a
,
z
]
S?[a,z]

SAMPLE INPUT
3
hlleo 1 3
ooneefspd 0 8
effort 1 4

SAMPLE OUTPUT
hlleo
spoonfeed
erofft
'''

test_cases = int(raw_input())
while test_cases > 0:
    string, start, end = map(str,raw_input().split())
    start = int(start)
    end = int(end)
    sorted_substring = sorted(string[start:end+1], reverse=True)
    print string[:start] + ''.join(sorted_substring) + string[end+1:len(string)]
    test_cases -= 1
