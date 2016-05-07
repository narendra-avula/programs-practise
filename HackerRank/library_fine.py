__author__ = 'Hinshitsu IT'

'''n = int(input())
for i in range(0,n):
    a, b = input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print (res)'''

sub_date = input()
act_date = input()
sub_date_year , sub_date_month , sub_date_date = sub_date.split()
act_date_year, act_date_month, act_date_date = act_date.split()
#print(sub_date_year, sub_date_month,sub_date_date)
#print(act_date_year, act_date_month, act_date_date)
if sub_date == act_date:
    print('0')
elif sub_date_year > act_date_year:
    print('10000')
elif sub_date_month > act_date_month:
    months = sub_date_month - act_date_month
    fine = 500 * months
    print(fine)
elif sub_date_date > act_date_date:
    days = sub_date_date -act_date_date
    fine = 15 * days
    print(fine)