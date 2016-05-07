__author__ = 'Hinshitsu IT'

e = int(input())
english = [int(x) for x in input().split()]
print(english)

f = int(input())
french = [int(x) for x in input().split()]
print(french)

print(len(set(english) | set(french) ) )
