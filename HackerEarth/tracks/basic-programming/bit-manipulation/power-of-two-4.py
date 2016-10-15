
import itertools

def get_sub_sets(array):
    return list(itertools.combinations(array, 2))

def power_of_two(sub_sets):
    for item in sub_sets:
        print list(item)
        x = reduce(lambda a, b: a and b, list(item))
        print x

test_cases = int(raw_input())
while(test_cases > 0):
    length_array = int(raw_input())
    numbers = map(int, raw_input().split())
    print numbers
    print get_sub_sets(numbers)
    sub_set_list = get_sub_sets(numbers)
    power_of_two(sub_set_list)
    test_cases -= 1