'''
1.4
https://open.kattis.com/problems/grassseed?tab=metadata
'''

c = float(input())

area = 0
for _ in range(int(input())):
    w,h = map(float, input().split())
    area += w * h

print(area * c)