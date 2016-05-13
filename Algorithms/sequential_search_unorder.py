__author__ = 'CustomFurnish'

def seq_search(numbers_list, search_element):
    for i in numbers_list:
        if i == search_element:
            return True
    return False


numbers_list = [1,5,8,3,51,0,2,9]
search_element = 0
if(seq_search(numbers_list, search_element)):
    print('Number found at index {}'.format(str(numbers_list.index(search_element))))
else:
    print('Number not found')
