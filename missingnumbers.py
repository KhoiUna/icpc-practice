'''
1.7
https://open.kattis.com/problems/missingnumbers
'''

seq = [int(input()) for _ in range(int(input()))]

missed = False

for n in range(1, seq[-1] + 1):
    if n not in seq: 
        print(n)
        missed = True


if not missed: print('good job')