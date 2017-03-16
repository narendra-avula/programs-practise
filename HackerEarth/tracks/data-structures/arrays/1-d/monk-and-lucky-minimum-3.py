__author__ = 'narendra'
'''
Monk just purchased an array
A
A having
N
N integers. Monk is very superstitious. He calls the array
A
A Lucky if the frequency of the minimum element is odd, otherwise he considers it Unlucky. Help Monk in finding out if the array is Lucky or not.

Input:
First line consists of a single integer
T
T denoting the number of test cases.
First line of each test case consists of a single integer
N
N denoting the size of array
A
A.
Second line of each test case consists of
N
N space separated integers denoting the array
A
A.

Output:
For each test case, print "Lucky" (without quotes) if frequency of minimum element is odd, otherwise print "Unlucky"(without quotes). Print a new line after each test case.

Constraints:

SAMPLE INPUT
2
5
8 8 9 5 9
5
3 3 3 5 3
SAMPLE OUTPUT
Lucky
Unlucky
Explanation
In first case, value of minimum element is
5
5 and it's frequency is
1
1 which is odd, so the array is Lucky.
In second case, value of minimum element is
3
3 and it's frequency is
4
4 which is even, so the array is Unlucky.
'''

def check_frequency(array):
    min_element = min(array)
    frequency = array.count(min_element)
    if frequency%2 == 0:
        print "Unlucky"
    else:
        print "Lucky"

if __name__ == '__main__':
    test_cases = int(raw_input())
    for _ in range(test_cases):
        length = int(raw_input())
        array = map(int, raw_input().split())
        check_frequency(array)
