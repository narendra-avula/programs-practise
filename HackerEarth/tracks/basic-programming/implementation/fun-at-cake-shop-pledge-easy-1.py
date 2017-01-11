__author__ = 'narendra'

'''
Darshak and Chandan went to a cake shop, and started finding a delicious cake to eat.
They decided to eat pancakes. Being misers, they end up with a discussion to challenge who will eat the last pancake.
They to follow a simple rule, and eat in rounds.
In the i'th round, Darshak eats i cakes whereas Chandan eats i2 cakes.

There are only X pancakes, you need to help the shopkeeper to find who had the last pancake, as he will pay the bill.

Input:
First line contains an integer X.

Output:
Output "Chandan" (without the quotes) if "Chandan" eats the last pancake ,"Darshak"(without the quotes) otherwise.

SAMPLE INPUT
12
SAMPLE OUTPUT
Chandan
Explanation
12 pancakes are eaten as :
Darshak Chandan
1 1
2 4
3 1 ( Only 1 remains)
Hence, Chandan consumes the last one.
'''

cakes = int(raw_input())
remaining_cakes = True
darshak = 1
chandan = 1
while remaining_cakes:
    darshak_cakes = darshak
    chandan_cakes = chandan
    remaining_cakes = cakes - ( darshak_cakes + chandan_cakes ** 2)
    print darshak_cakes, chandan_cakes**2 , remaining_cakes
    darshak += 1
    chandan += 1
    if remaining_cakes < 0:
        remaining_cakes = False