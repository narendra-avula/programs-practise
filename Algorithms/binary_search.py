__author__ = 'CustomFurnish'

def binary_search(numbers_list, search_element):
    # print('Hello')
    start = 0
    last = len(numbers_list)-1
    found = False
    count = 0
    while(start <= last) and not found:
        middle = (start + last)//2
        if numbers_list[middle] == search_element:
            found = True
        elif search_element > numbers_list[middle]:
            start = middle + 1
        elif search_element < numbers_list[middle]:
            last = middle - 1

        count += 1
    return found, count


numbers_list = [17,20,26,31,44,54,65,77,93]
search_element = int(input('Enter Number'))
found , comparisions = binary_search(numbers_list, search_element)
if(found):
    print('Number found at index {} in {} comparisions'.format( str(numbers_list.index(search_element)),comparisions ))

else:
    print('Number not found')
