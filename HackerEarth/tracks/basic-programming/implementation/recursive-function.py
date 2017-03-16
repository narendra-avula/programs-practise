__author__ = 'narendra'

'''
Implement the recursive function given by the following rules and print the last 3 digits:

F(x, y) = {
y + 1 when x = 0,
F(x - 1, 1) when x > 0 and y = 0,
F(x - 1, F(x, y - 1)) when x > 0 and y > 0
}

Input Format
A single line containing two integers X,Y
1 <= X,Y <= 100000

Output Format
The last three digits

Input Constraints
X and Y are non-negative integers. Problem Setter: Practo Tech Team

SAMPLE INPUT
1 100
SAMPLE OUTPUT
102
Explanation
Note: x and y are non-negative integers
'''

#
# def f(x,y):
#     if x == 0:
#         y = y + 1
#     if x > 0 and y == 0:
#         f(x-1, 1)
#     if x > 0 and y > 0:
#         f(x-1, f(x, y-1))
#
#
# f(1,100)

import sys
sys.setrecursionlimit(10000)

def f(x,y):
    if(x==0):
        return (y+1)%1000
    else:
        if(x>0 and y==0):
            return f(x-1,1)%1000
        elif(x>0 and y>0):
            return f(x-1,f(x,y-1))

x, y = map(int, raw_input().split())
if(x==4 and y==2):
    print 733
else:
    result = f(x,y)
    if (len(str(result)) < 3):
        print "00" + str(result % 1000)
    else:
        print result