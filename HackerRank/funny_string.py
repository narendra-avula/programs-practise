__author__ = 'Hinshitsu IT'
'''
2
acxz
bcxz

Funny
Not Funny
'''
cases = int(input())
for case in range(cases):
    string = input()
    reverse_string = string[::-1]
    n = len(string)
    for i in range(1, n):
        d1 = abs(ord(string[i]) - ord(string[i - 1]))
        d2 = abs(ord(reverse_string[i]) - ord(reverse_string[i - 1]))
        if d1 != d2:
            print("Not Funny")
            break
    else:
        print("Funny")