'''
1.7
https://open.kattis.com/problems/simonsays
'''

res = ''

for _ in range(int(input())):
    filtered = input().split('Simon says ')
    if len(filtered) == 1: continue

    res += ' '.join(filtered) + '\n'


print(res)