__author__ = 'Hinshitsu-IT'
'''
Cash Register.
Challenge Description:
The goal of this challenge is to design a cash register program. You will be
given two float numbers. The first is the purchase price (PP) of the item. The
second is the cash (CH) given by the customer. Your register currently has the
following bills/coins within it:
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
The aim of the program is to calculate the change that has to be returned to
the customer.

Input sample:

Your program should accept as its first argument a path to a filename. The
input file contains several lines. Each line is one test case. Each line
contains two numbers which are separated by a semicolon. The first is the
Purchase price (PP) and the second is the cash(CH) given by the customer. eg.

15.94;16.00
17;16
35;35
45;50

Output sample:

For each set of input produce a single line of output which is the change to be
returned to the customer. In case the CH < PP, print out ERROR. If CH == PP,
print out ZERO. For all other cases print the amount that needs to be returned,
in terms of the currency values provided. The output should be sorted in
highest-to-lowest order (DIME,NICKEL,PENNY). eg.
NICKEL,PENNY
ERROR
ZERO
FIVE

'''
money = {
    .01    : 'PENNY',
    .05    : 'NICKEL',
    .10    : 'DIME',
    .25    : 'QUARTER',
    .50    : 'HALF DOLLAR',
    1.00   : 'ONE',
    2.00   : 'TWO',
    5.00   : 'FIVE',
    10.00  : 'TEN',
    20.00  : 'TWENTY',
    50.00  : 'FIFTY',
    100.00 : 'ONE HUNDRED'
}

test_cases = open('cash_register.txt','r')
for test in test_cases:
    pp, ch = (float(i) for i in test.split(';'))
    if ch < pp:
        print('ERROR')
    elif ch == pp:
        print('ZERO')
    else:
        change = ch - pp
        result = []
        for i in sorted([c for c in money.keys() if c <= change], reverse=True):
            result.append(int(change / i) * [money[i]])
            change = round(change % i, 2)
            if not change:
                break
        print (','.join(sum(result, [])))


# for test in test_cases:
#     PP, CH = (float(i) for i in test.split(';'))
#     if CH < PP:
#         print 'ERROR'
#     elif CH == PP:
#         print 'ZERO'
#     else:
#         change, output = CH - PP, []
#         for i in sorted([c for c in money.keys() if c <= change], reverse=True):
#             output.append(int(change / i) * [money[i]])
#             change = round(change % i, 2)
#             if not change:
#                 break
#         print ','.join(sum(output, []))