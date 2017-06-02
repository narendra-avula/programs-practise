__author__ = 'narendra'
'''
We consider a word, , to be beautiful if the following two conditions are satisfied:

No two consecutive characters are the same.
No two consecutive characters are in the following vowel set: a, e, i, o, u, y. Note that we consider y to be a vowel in this challenge.
For example:

image

The string batman is beautiful because it satisfies the given criteria; however, apple has two consecutive occurrences of the same letter (pp) and beauty has three consecutive vowels (eau), so those words are not beautiful.

Given , print Yes if it is beautiful or No if it is not.

Input Format

A single string denoting .

Constraints

 consists of lowercase English alphabetic letters only (i.e., a through z).
Output Format

Print Yes if  is beautiful, or No if it is not.

Sample Input 0

abacaba
Sample Output 0

Yes
Explanation 0

Every pair of consecutive characters consists of one vowel and one consonant, so the word is beautiful and we print Yes.

Sample Input 1

badd
Sample Output 1

No
Explanation 1

There are two consecutive occurrences of d, so it is not beautiful and we print No.

Sample Input 2

yes
Sample Output 2

No
Explanation 2

The first pair of letters (y and e) both appear in our set of vowel characters, so the word is not beautiful and we print No.
'''

import sys


w = raw_input().strip()
# Print 'Yes' if the word is beautiful or 'No' if it is not.
vowel_set = list('aeiouy')
result = None
if len(w) > 2:
    for i in range(len(w) - 1):
        if w[i] != w[i + 1] and (w[i] not in vowel_set or w[i + 1] not in vowel_set):
            result = "Yes"
        else:
            result = 'No'
            break
else:
    result = 'Yes'

print result