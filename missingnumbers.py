'''
1.7
https://open.kattis.com/problems/missingnumbers
'''

seq = [int(input()) for _ in range(int(input()))]

cache = []
for n in seq:
    if n-1 not in seq and n-1 not in cache and n-1 > seq[0]:
        cache.append(n-1)
        print(n-1)
    if n+1 not in seq and n+1 not in cache and n+1 < seq[-1]:
        cache.append(n+1)
        print(n+1)

if len(cache) == 0: print('good job')