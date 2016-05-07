__author__ = 'Hinshitsu-IT'
'''
1
4 5
9 7 5 3
8 6 4 2 0

9 8 7 6 5 4 3 2 0
'''

for _ in range(int(input())):
    m, n = map(int,input().split())
    m_list = list(map(int,input().split()))
    n_list = list(map(int,input().split()))
    print(' '.join(str(i) for i in sorted(m_list+n_list,reverse=True)))