'''
1.3
https://open.kattis.com/problems/sorttwonumbers?tab=metadata
'''

a,b = map(int, input().split())

if a > b:
    print(b,a)
else:
    print(a,b)