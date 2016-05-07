__author__ = 'Hinshitsu-IT'
'''
Sample Input

aabbbccde

Sample Output

b 3
a 2
c 2

'''

from collections import Counter
d = list(input().rstrip())
#print(d)
opt = []
for i in d:
    print(i)
    if i not in d:
        opt.append(i)

print(opt)

# for w in sorted(d, key=d.get, reverse=True):
#   if d[w] > 1:
#     print (w, d[w])