__author__ = 'narendra'
'''
Monk introduces the concept of palindrome saying,"A palindrome is a sequence of characters which reads the same backward or forward."
Now, since he loves things to be binary, he asks you to find whether the given string is palindrome or not. If a given string is palindrome, you need to state that it is even palindrome (palindrome with even length) or odd palindrome (palindrome with odd length).

Input:
The first line consists of
T
T, denoting the number of test cases.
Next follow
T
T lines, each line consisting of a string of lowercase English alphabets.

Output:
For each string , you need to find whether it is palindrome or not.
If it is not a palindrome, print NO.
If it is a palindrome, print YES followed by a space; then print EVEN it is an even palindrome else print ODD.
Output for each string should be in a separate line.
See the sample output for clarification.

Constraints:

SAMPLE INPUT
3
abc
abba
aba
SAMPLE OUTPUT
NO
YES EVEN
YES ODD
Explanation
The first string is not a palindrome.
The second and third strings are palindromes of even and odd lengths respectively.
'''

'''
Editorial:

Brief Description: Check whether the string is palindrome or not, and if it is then check whether it has even length or odd.

Prerequisite: None

Hint: Reverse the string and then check if it is equal to the original string.

Difficulty: Very Easy

Detailed Editorial:

First reverse the string and store it in another variable, then check whether the

reversed string is equal to the original string or not. If both are equal, it means string is a palindrome.

Then check whether the length of string is even or odd.

Pseudo Code:

reverse_string = ""

for (i from  original_string.length()-1 to 0)
    reverse_string + = original_string[ i ]

if(reverse_string == original_string) //palindrome

         if(original_string.length()%2) //odd
                        print "Yes Odd"
         else
                        print "Yes Even"
else
    print "No"
There exists a solution, where you can traverse upto half of the string and can check whether the string is palindrome or not.

Time Complexity:
O
(
N
)
O(N), where
N
N is the length of string.

Space Complexity:
O
(
N
)
'''

def check_palindrome(string):
    if string == string[::-1]:
        if ( len(string) % 2 ) == 0:
            print "YES EVEN"
        else:
            print "YES ODD"
    else:
        print "NO"

if __name__ == '__main__':
    test_cases = int(raw_input())
    for _ in range(test_cases):
        check_palindrome(raw_input())