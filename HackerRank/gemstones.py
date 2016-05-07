__author__ = 'CustomFurnish'
'''
3
abcdde
baccd
eeabg

2
'''
string_list = []
for _ in range(int(input())):
    string_list.append(list(input()))
# print(string_list)
print(len(set(string_list[0]).intersection(*string_list)))