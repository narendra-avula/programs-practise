__author__ = 'narendra'
'''
Objective
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

Recursive Method for Calculating Factorial
Task
Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer,  (the argument to pass to factorial).

Constraints

Your submission must contain a recursive function named factorial.
Output Format

Print a single integer denoting .

Sample Input

3
Sample Output

6
Explanation

Consider the following steps:

From steps  and , we can say ; then when we apply the value from  to step , we get . Thus, we print  as our answer.
'''
def recursive_factorial(number):
    if number < 1:
        return 1
    else:
        fact_number = number * recursive_factorial(number-1)
        return fact_number


def read_input_data():
    number = int(raw_input())
    print recursive_factorial(number)

if __name__ == '__main__':
    read_input_data()


'''
C
#include <stdio.h>

int factorial(int n){

    return (n == 1) ? 1 : n * factorial(n - 1);

};

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", factorial(n));
    return 0;
}


C++
#include <iostream>

using namespace std;

int factorial(int n) {
    return (n > 1) ? n * factorial(n - 1) : 1;
}

int main() {
    int n;
    cin >> n;
    cout << factorial(n);
    return 0;
}


Java
public class Solution {

    public static int factorial(int n){
        return (n > 1) ? n * factorial(n - 1) : 1;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        System.out.println(factorial(n));
    }
}
'''