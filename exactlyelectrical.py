'''
2.2
https://open.kattis.com/problems/exactlyelectrical
'''
[a, b] = [int(i) for i in input().split(' ')]
[c, d] = [int(i) for i in input().split(' ')]
t = int(input())

diff = t - (abs(a-c) + abs(b-d))
if diff >= 0 and diff % 2 == 0:
    print('Y')
else:
    print('N')
