__author__ = 'Naidu'
'''
Oz has a list arr[] of M integers. He has to find all integers K such that :

1) K > 1
2) arr[1]%K = arr[2]%K = arr[3]%K = ... = arr[M]%K where '%' is a modulus operator
Help Oz to find all such K's.

Input :
First line of input contains an integer M. Then M lines follow each containing one integer of the list. Input data is such that at least one integer K will always exist.

Output :
Output all possible integers K separated by space in increasing order.

Constraints :
- 2<= M <=100
- 1< value of each integer <109
- All integers will be distinct

SAMPLE INPUT
3
38
6
34

SAMPLE OUTPUT
2 4
'''

number = int(raw_input())

