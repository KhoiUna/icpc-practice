'''
1.4
https://open.kattis.com/problems/datum?tab=metadata
'''

dow = {
    0: 'Thursday',
    1: 'Friday',
    2: 'Saturday',
    3: 'Sunday',
    4: 'Monday',
    5: 'Tuesday',
    6: 'Wednesday',
}
days_in_month = {
  1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

d,m = map(int, input().split())

days_diff = d
for month in range(1,m):
    days_diff += days_in_month[month]

print(dow[(days_diff - 1) % 7])
