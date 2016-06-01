__author__ = 'Naidu'
'''
Xsquare loves to play with strings a lot. Today, he has two strings S1 and S2 both consisting of lower case alphabets. Xsquare listed all subsequences of string S1 on a paper and all subsequences of string S2 on a separate paper. Xsquare wants to know whether there exists a string which is listed on both the papers.

Xsquare thinks that this task is pretty boring and handed it to you. Please accomplish this task on his behalf.

Input

First line of input contains a single integer T denoting the number of test cases. Each test case consists of two lines. First line of each test case contains a string denoting string S1. Next line of each test case contains a string denoting string S2.

Output

For each test case, Print Yes if both papers contain a common string otherwise Print No.

Constraints

1 ? T ? 105

1 ? |S1| ? 105

1 ? |S2| ? 105

Sum of |S1| over all test case does not exceed 5*105

Sum of |S2| over all test case does not exceed 5*105

Subtasks

Subtask1 : sum of |S1|,|S2| over all test cases does not exceed 103 (25 pts)
Subtask2 : sum of |S1|,|S2| over all test cases does not exceed 104 (25 pts)
Subtask3 : sum of |S1|,|S2| over all test cases does not exceed 5*105 (50 pts)

SAMPLE INPUT
2
phackerekarthj
jhakckerearthp
hello
buy

SAMPLE OUTPUT
Yes
No
'''

# def diff(first, second):
#         second = set(second)
#         return [item for item in first if item not in second]

def is_subsequence(s1, s2):
    if len(s1) > len(s2):
        a, b = s1, s2
    else:
        a, b = s2, s1

    a = list(a)
    b = list(b)

    for x in a:
        if x in b:
            continue
        else:
            return "No"
    return "Yes"

test_cases = int(raw_input())
while test_cases > 0:
    s1 = raw_input()
    s2 = raw_input()
    # print diff(s1, s2)
    print is_subsequence(s1, s2)
    test_cases -= 1
