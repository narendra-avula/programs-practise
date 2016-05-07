__author__ = 'Hinshitsu-IT'
'''
4
ab
cd
ef
cd

3
'''
l = []
for _ in range(int(input())):
    l.append(input())
print(len(set(l)))

