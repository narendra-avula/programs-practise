__author__ = 'Hinshitsu-IT'
'''
2
1 10
3 5
'''
def sieve( n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    for i in range(2, int(round(n**0.5)) + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

# for _ in range(int(input())):
#     start, end = map(int, input().split())

test = list(sieve(100))
