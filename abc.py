'''
2.1
https://open.kattis.com/problems/abc
'''
[a,b,c] = sorted([int(i) for i in input().split()])

for i in input():
    if i == 'A':
        print(a,end=' ')
    elif i == 'B':
        print(b,end=' ')
    else:
        print(c,end=' ')