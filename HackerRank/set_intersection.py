__author__ = 'Hinshitsu IT'

e = int(input())
english = set(input().split())
print(english)

f = int(input())
french = set(input().split())
print(french)

print(len(english & french ) )
