__author__ = 'CustomFurnish'

'''
Input:
4 7 10
2 6 18
0 0 0

Output:
AP 13
GP 54

'''

# a1, a2, a3 = map(int,input().split())
# if abs(a2-a1) == abs(a3-a2):
#     a_ap = a3 + abs(a3-a2)
#     print('AP '+ str(a_ap))
#
# if a2/a1 == a3/a2:
#     a_gp = a3 * (a3//a2)
#     print('GP '+ str(a_gp))

test_cases = []
flag = True
while flag:
    a = list(map(int,input().split()))
    # print(len(set(a)))
    if len(set(a)) == 1:
        break
    test_cases.append(a)

# print(test_cases)

for i in test_cases:
    # print(i[0])
    a1, a2, a3 = i[0], i[1], i[2]
    if abs(a2-a1) == abs(a3-a2):
        a_ap = a3 + abs(a3-a2)
        print('AP '+ str(a_ap))

    if a2/a1 == a3/a2:
        a_gp = a3 * (a3//a2)
        print('GP '+ str(a_gp))
