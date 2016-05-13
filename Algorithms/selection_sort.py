__author__ = 'CustomFurnish'

def selection_sort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       position_of_max = 0
       print('Pass num {}'.format(fillslot))
       for location in range(1,fillslot+1):
           if alist[location] > alist[position_of_max]:
               position_of_max = location
       alist[fillslot], alist[position_of_max] = alist[position_of_max], alist[fillslot]
       print(alist)

alist = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
print(alist)
selection_sort(alist)
print('Final')
print(alist)