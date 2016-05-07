__author__ = 'Hinshitsu-IT'
'''
2
RKKRK
RKKR

4
4
'''
for _ in range(int(input())):
    input_list = list(input())
    for i in range(1,len(input_list)):
        if input_list[i] =='R' :
            input_list[i]= 'K'
        else :
            input_list[i] ='R'
    print(input_list.count('R'))