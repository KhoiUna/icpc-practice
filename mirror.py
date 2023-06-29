'''
1.7
https://open.kattis.com/problems/mirror
'''

for i in range(int(input())):
    r,c = map(int, input().split())
    
    original = [list(input()) for _ in range(r)]
    res = original

    print('Test', i+1)
    
    # Going backward
    for r_idx in range(r-1, -1, -1):
        for c_idx in range(c-1, -1, -1):
           print(original[r_idx][c_idx], end='')

        print()