__author__ = 'narendra'

'''
Carl, Caroline, Helen, and Han are four friends sharing a one-room workspace. The workspace has a single thermostat which they can set to any integer temperature between  degrees to  degrees Fahrenheit, inclusive.

The four friends can't agree on the room's temperature! Carl and Caroline don't want it to be too cold, while Helen and Han don't want it to be too hot. Specifically:

Carl wants it to be at least  degrees Fahrenheit.
Caroline wants it to be at least  degrees Fahrenheit.
Helen wants it to be at most  degrees Fahrenheit.
Han wants it to be at most  degrees Fahrenheit.
Given , , , and , is there a satisfactory temperature that all four friends will be happy with? If it's possible, print YES; otherwise, print NO.

Input Format

Four space-separated integers describing the respective values of , , , and .

Constraints

Output Format

Print YES if it's possible to satisfy all four friends' conditions; otherwise, print NO instead.

Sample Input 0

50 40 70 60
Sample Output 0

YES
Explanation 0

The four friends have the following temperature preferences:

Carl wants it to be at least  degrees.
Caroline wants it to be at least  degrees.
Helen wants it to be at most  degrees.
Han wants it to be at most  degrees.
image

Any temperature between  and  degrees will satisfy all four friends, so we print YES.

Sample Input 1

55 66 66 77
Sample Output 1

YES
Explanation 1

The four friends have the following temperature preferences:

Carl wants it to be at least  degrees.
Caroline wants it to be at least  degrees.
Helen wants it to be at most  degrees.
Han wants it to be at most  degrees.
image

A temperature of exactly  degrees will satisfy all four friends, so we print YES.

Sample Input 2

80 80 40 40
Sample Output 2

NO
Explanation 2

In this test case, Carl wants the temperature to be at least  and Helen wants it to be at most . There is no temperature that is both  and , so we print NO because no satisfactory temperature exists.


'''

#!/bin/python

import sys

def isSatisfiable(c1, c2, h1, h2):
    if max(c1, c2) <= min(h1, h2):
        return "YES"
    else:
        return "NO"

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = raw_input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)

c1, c2, h1, h2 = map(int, raw_input().split())
print ('YES' if max(c1, c2) <= min(h1, h2) else 'NO' )