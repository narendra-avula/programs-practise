__author__ = 'CustomFurnish'
'''
Cabernet Merlot Noir | ot
Chardonnay Sauvignon | ann
Shiraz Grenache | o

Merlot
Chardonnay Sauvignon
False

'''

def comp(list1, list2):
    count = 0
    for val in list1:
        if val in list2:
            count +=1
    if count == len(list1):
        return True
    else:
        return False

# print(comp( ['o', 't'], ['C', 'a', 'b', 'e', 'r', 'n', 'e', 't'] ))

test_cases = open('CHARDONNAY_OR_CABERNET.txt','r')
for test in test_cases:
    string, sub_string = test.strip().split('|')
    sub_string = list(sub_string.strip())
    # print(string,sub_string )
    words = [list(word) for word in string.split()]
    # print(list(words))
    result = []
    for word in words:
        if comp(sub_string, word):
            result.append(''.join(word))
    if result:
        print(' '.join(result))
    else:
        print('False')

