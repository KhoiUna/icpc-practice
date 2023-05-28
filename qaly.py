'''
1.3
https://open.kattis.com/problems/qaly

Input:        
5
1.0 12.0
0.7 5.2
0.9 10.7
0.5 20.4
0.2 30.0

Output: 41.470
'''

lines = int(input())

total = 0 
for i in range(lines):
    [q,y] = [float(i) for i in input().split(' ')]
    total += q*y

print(total)