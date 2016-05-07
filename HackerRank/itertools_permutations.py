__author__ = 'Hinshitsu-IT'

'''
HACK 2

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

'''
# from itertools import permutations
# string = input().split()
# text = string[0]
# number = int(string[1])
# text_characters = list(text)
# text_characters.sort()
# #print(text_characters)
# #print(list(permutations(text_characters,2)))
# print(''.join(e) for e in permutations(text_characters, number))


from itertools import permutations
a = input()
for e in permutations(sorted(a),len(a)):
    print(''.join(e), end=' ')
