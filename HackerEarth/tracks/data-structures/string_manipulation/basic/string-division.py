__author__ = 'Naidu'
'''
Kevin has a string S consisting of N lowercase English letters.

Kevin wants to split it into 4 pairwise different non-empty parts. For example, string "happynewyear" can be splitted into "happy", "new", "ye" and "ar". He can't delete any characters or change the order of the characters.

Help Kevin and find if there exist at least one possible spliting.

Input format:

The first line of input will contain an integer T, denoting the number of test cases. Each of the next T lines contains a string S.

Output format:

For every test case output "YES" if it is possible to split the string and "NO" otherwise.

Constraints:

1 ? T ? 100
1 ? N ? 1000
N ? 20 in test data worth 40% of all points
SAMPLE INPUT
2
ababca
aaabb
SAMPLE OUTPUT
YES
NO
'''

test_cases = int(raw_input())
while test_cases > 0:
    string = raw_input()
    unique_letters = set(list(string))
    # print unique_letters
    if len(unique_letters) > 2:
        print "YES"
    else:
        print "NO"