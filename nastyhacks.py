'''
1.4
https://open.kattis.com/problems/nastyhacks
'''

for _ in range(int(input())):
    r,e,c = map(int, input().split())
    
    if c < r:
        print('does not matter')
    elif e > r and e > c:
        print('advertise')
    elif c > e:
        print('do not advertise')