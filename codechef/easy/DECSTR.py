__author__ = 'Narendra Avula'
'''
All submissions for this problem are available.

Statement

You need to find a string which has exactly K positions in it such that the character at that position comes alphabetically later than the character immediately after it. If there are many such strings, print the one which has the shortest length. If there is still a tie, print the string which comes the lexicographically earliest (would occur earlier in a dictionary).
Input

The first line contains the number of test cases T. Each test case contains an integer K (? 100).
Output

Output T lines, one for each test case, containing the required string. Use only lower-case letters a-z.
Sample Input

2
1
2
Sample Output

ba
cba
'''

# from string import ascii_lowercase
# string = ascii_lowercase
# # print(string)
# for _ in range(int(input())):
#     number = int(input())
#     print(string[:number+1][::-1])
#include <stdio.h>
#include <string.h>
# int main()
# {
# 	int i,T,K,Times;
# 	scanf("%d", &T);
# 	while(T--)
# 	{
# 		scanf("%d", &K);
# 		Times = K/25;
#         if(K%25 == 0 && K) goto Jump;
#         for(i= 97 + K%25 ; i>=97 ;i--)printf("%c", i);
#   Jump: while(Times--) printf("zyxwvutsrqponmlkjihgfedcba");
#         printf("\n");
# 	}
# 	return 0;
# }
# for _ in range(int(input())):
#     number = int(input())
#     times = number//25
#     if (number % 25 == 0 ) and number:
#         for

