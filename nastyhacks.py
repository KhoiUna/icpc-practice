'''
1.4
https://open.kattis.com/problems/nastyhacks
'''

for _ in range(int(input())):
    r,e,c = map(int, input().split())
    
    if e - r == c:
        print('does not matter')
    elif e - r > c:
        print('advertise')
    else:
        print('do not advertise')