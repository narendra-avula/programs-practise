__author__ = 'Hinshitsu-IT'
'''
3
1
10
0 1 2 3 2 1 7 8 9 6
2
5 5
3
3 5 1

5
2
1
'''
# for _ in range(input()):
# 	num=int(raw_input())
# 	lst=[]
# 	lst=raw_input().split()
# 	lst3=[]
# 	for i in lst:lst3.append(i)
# 	lst3.reverse()
# 	lst2=set(lst)
# 	maxx=1
# 	for i in lst2:
# 		maxx=max((num-lst3.index(i))-lst.index(i),maxx)
# 	print maxx

for _ in range(int(input())):
    num = int(input())
    numbers = list(map(int, input().split()))

    numbers_2 = []
    for i in numbers:numbers_2.append(i)
    numbers_2.reverse()
    print(numbers_2)

    numbers_3 = set(numbers)
    print(numbers_3)
    maxx = 1
    for i in numbers_2:
        maxx=max((num-numbers_2.index(i))-numbers.index(i),maxx)
    print (maxx)