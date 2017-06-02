__author__ = 'narendra'

'''

https://www.hackerrank.com/contests/w32/challenges/fight-the-monsters

Jason is trapped in a forest with  hungry monsters and must use his trusty blaster to defend himself! Each monster  has a health value, . Jason can discharge his blaster at a monster once per second and reduce its health points by  units. Once a monster's health points become , it dies.

Given the health values for each monster and an integer, , can you determine the maximum number of monsters he can kill in  seconds? Assume Jason always hits his target!

Input Format

The first line consists of three space-separated integers describing the respective values of , , and .
The second line consists of  space-separated integers describing the values of .

Constraints

Output Format

Print an integer denoting the maximum number of monsters Jason can kill in  seconds.

Sample Input 0

7 8 6
16 19 7 11 23 8 16
Sample Output 0

4
Explanation 0

We want to find the maximum number of monsters we can kill in  seconds using a blaster that does units of damage per second. The diagram below depicts the array of initial health values, :

image
The optimal approach is as follows:

Shoot monster  so , monster  dies, and  becomes :

image
Shoot monster  so , monster  dies, and  becomes :

image
Shoot monster  so  and  becomes :

image
Shoot monster  again so , monster  dies, and  becomes :
image
Shoot monster  so  and  becomes :
image
Shoot monster  again so , monster  dies, and  becomes : image
Thus, we print  as the maximum number of monsters we can kill in the given time period.
'''

import sys

def getMaxMonsters(n, hit, t, h):
    # Complete this function
    for _ in range(t):
        min_element = h.index(min(i for i in h if i > 0))
        hit_monster = h[min_element] - hit
        h[min_element] = hit_monster
    count = 0
    for value in h:
        if value <= 0:
            count += 1
    return o


n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
# n, hit, t = 7, 8, 6
# h = [16, 19, 7, 11, 23, 8, 16]
result = getMaxMonsters(n, hit, t, h)
print(result)