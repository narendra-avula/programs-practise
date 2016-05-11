__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.
Class ID	Ship Class
B or b	BattleShip
C or c	Cruiser
D or d	Destroyer
F or f	Frigate
Input

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains a character.
Output

Display the Ship Class depending on ID.
Constraints

1 ? T ? 1000
Example

Input

3
B
c
D

Output
BattleShip
Cruiser
Destroyer
'''

for _ in range(int(input())):
    id = input()
    if id == 'B' or id == 'b':
        print('BattleShip')
    elif id == 'C' or id == 'c':
        print('Cruiser')
    elif id == 'D' or id == 'd':
        print('Destroyer')
    elif id == 'F' or id == 'f':
        print('Frigate')