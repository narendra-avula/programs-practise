__author__ = 'Naidu'
'''
You have been given
3
3 integers
l
l,
r
r and
k
k. Find how many numbers between
l
l and
r
r (both inclusive) are divisible by
k
k. You do not need to print these numbers, you just have to find their count.

Input Format
The first and only line of input contains 3 space separated integers
l
l,
r
r and
k
k.

Output Format
Print the required answer on a single line.

Constraints
 1
?
l
?
r
?
1000
1?l?r?1000
 1
?
k
?
1000
1?k?1000

SAMPLE INPUT
1 10 1
SAMPLE OUTPUT
10

There are multiple ways to solve this problem. The easiest one is to iterate over the entire range and check each number. This gives us a time complexity of
O
(
N
)
O(N) where
N
N is the size of the range. However, this problem can also be solved in
O
(
1
)
O(1) time which might be helpful for larger constraints. The number of numbers divisible by a certain number
k
k in the range from
1
1 to
r
r is
r
/
k
r/k Thus we can first find the number of numbers divisible by
k in the range from
1 to
r and then subtract from it the numbers divisible by
k in the range from
l?1 to obtain the answer.

Answer :
(r/k)?((l?1/k))

import java.io.*;
import java.util.*;
class example_2
{
    static Scanner sc=new Scanner(System.in);

    public static void main(String args[]) throws Exception
    {
        int l=sc.nextInt(),r=sc.nextInt(),k=sc.nextInt();
        System.out.println((r/k)-((l-1)/k));
    }
}
'''

# l, r, k = map(int,raw_input().split())
# count = 0
# for i in range(l, r+1):
#     if i % k == 0:
#         count += 1
# print count

l, r, k = map(int,raw_input().split())
print (r/k)-((l-1)/k)