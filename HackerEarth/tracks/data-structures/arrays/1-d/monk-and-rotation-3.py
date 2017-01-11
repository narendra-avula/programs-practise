__author__ = 'narendra'
'''
Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array
A
A of size
N
N and an integer
K
K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

Input:
The first line will consists of one integer
T
T denoting the number of test cases.
For each test case:
1) The first line consists of two integers
N
N and
K
K,
N
N being the number of elements in the array and
K
K denotes the number of steps of rotation.
2) The next line consists of
N
N space separated integers , denoting the elements of the array
A
A.
Output:
Print the required array.

Constraints:

SAMPLE INPUT
1
5 2
1 2 3 4 5
SAMPLE OUTPUT
4 5 1 2 3
Explanation
Here
T
T is 1, which means one test case.
 N
=
5
N=5 denoting the number of elements in the array and
K
=
2
K=2, denoting the number of steps of rotations.
The initial array is:
1,2,3,4,5
In first rotation,
5
5 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be

5,1,2,3,4
In second rotation,
4
4 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be
4,5,1,2,3
'''

def rotation(array, step):
    if step > len(array):
        step = step%len(array)
    result =  array[len(array)-step:] + array[:len(array)-step]
    print ' '.join(str(i) for i in result)

if __name__ == '__main__':
    test_cases = int(raw_input())
    for _ in range(test_cases):
        array_size, step = map(int, raw_input().split())
        array = map(int, raw_input().split())
        rotation(array, step)


