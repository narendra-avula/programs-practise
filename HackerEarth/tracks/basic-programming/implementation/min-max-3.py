__author__ = 'narendra'
'''
Given an array of integers . Check if all the numbers between minimum and maximum number in array exist's within the array .

Print 'YES' if numbers exist otherwise print 'NO'(without quotes).

Input:

Integer N denoting size of array

Next line contains N space separated integers denoting elements in array

Output:

Output your answer

Constraints:

1<= N <= 1000

1<= a[i] <= 100

SAMPLE INPUT
6
4 2 1 3 5 6
SAMPLE OUTPUT
YES
'''

array_size = int(raw_input())
numbers = map(int, raw_input().split())
start = min(numbers)
end = max(numbers)
min_max = ''
for num in numbers:
    if num in range(start+1, end+1):
        min_max = "YES"
    else:
        min_max =  "NO"
        break
print min_max
