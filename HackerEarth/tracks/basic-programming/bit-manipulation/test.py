__author__ = 'Naidu'

# import itertools
#
# def list_of_combs(arr):
#     """returns a list of all subsets of a list"""
#     combs = []
#     for i in xrange(1, len(arr)+1):
#         listing = [list(x) for x in itertools.combinations(arr, i)]
#         combs.extend(listing)
#     return combs
#
# print list_of_combs([1,2, 3])

# import itertools
#
# for i in itertools.count(10,20):
#     print i

def infinite_numbergenerator():
    n = 0
    while True:
         yield n
         n += 1

for i in infinite_numbergenerator():
    if i == 522522:
        quit()
    else:
        print i