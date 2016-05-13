__author__ = 'CustomFurnish'

def seq_search(numbers_list, search_element):
    count = 0
    for i in numbers_list:
        if i == search_element and i >= search_element:
            return True, count
        count += 1
    return False, count


numbers_list = [0,2,5,7,9,10,14,16,20,67]
search_element = 15
# print(seq_search(numbers_list, search_element))
found , comparisions = seq_search(numbers_list, search_element)

if(found):
    print('Number found at index {} in {} comparisions'.format( str(numbers_list.index(search_element)),comparisions ))

else:
    print('Number not found')
