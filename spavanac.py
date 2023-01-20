# https://open.kattis.com/contests/npytjx/problems/spavanac

'''
Input:
  hour
  minute
'''

[hour, minute] = input().split(' ')
hour = int(hour)
minute = int(minute)
time = hour * 60 + minute

output = time - 45
hour = output // 60
minute = output - hour * 60

if hour < 0:
    hour += 24

output = f'{hour} {minute}'

print(output)
