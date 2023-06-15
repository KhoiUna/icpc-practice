'''
1.4
https://open.kattis.com/problems/cprnummer?tab=metadata

Input:
- first six digits represent the person's day of birth.
- The following four digits are a sequence number.
- modulo 11 rule
'''

s = ''.join(input().split('-'))

nums = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

res = 0
for i in range(len(s)):
    res += nums[i] * int(s[i])

if res % 11 == 0: print(1)
else: print(0)