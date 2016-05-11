__author__ = 'CustomFurnish'
'''
Input:

5
toioynnkpheleaigshareconhtomesnlewx
0
3
ttyohhieneesiaabss
0

Output:

theresnoplacelikehomeonasnowynightx
thisistheeasyoneab

'''

def split_string(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

test_cases = []
test = []
flag = True
while flag:
    number = int(input())
    if number == 0:
        break
    string = input()
    result = split_string(string, number)
    # print(result)
    for i in range(len(result)):
        if i % 2 != 0 :
            result[i] = result[i][::-1]
    print(result)
    for i in result:
        test.append(list(i))
    print(test)
    # print(len(result))
    # for i in range(len(result)):
    #     # print(result[i])
    #     # print(len(result[i]))
    #     for j in range(len(result[i])):
    #         test.append(result[i][j])
    # print(test)


# s = 'toioynnkpheleaigshareconhtomesnlewx'



# print(splitCount(s, 5))