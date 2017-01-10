__author__ = 'narendra'

'''
The great Kian is looking for a smart prime minister. He's looking for a guy who can solve the OLP (Old Legendary Problem). OLP is an old problem (obviously) that no one was able to solve it yet (like P=NP).

But still, you want to be the prime minister really bad. So here's the problem:

Given the sequence a1, a2, ..., an find the three values a1 + a4 + a7 + ..., a2 + a5 + a8 + ... and a3 + a6 + a9 + ... (these summations go on while the indexes are valid).

Input

Output

Print three values in one line (the answers).

SAMPLE INPUT
5
1 2 3 4 5

SAMPLE OUTPUT
5 7 3

'''


input = int(raw_input())
sequence = map(int, raw_input().split())
print sum(sequence[0::3]), sum(sequence[1::3]), sum(sequence[2::3])