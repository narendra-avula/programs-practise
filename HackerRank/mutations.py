__author__ = 'Hinshitsu IT'

word = input()
index1, letter = input().split()
index1 = int(index1)
print(word[:index1]+letter+word[index1+1:])