'''
1.6
https://open.kattis.com/problems/rectanglearea
'''
[x1, y1, x2, y2] = [float(i) for i in input().split(' ')]

area = (x2 - x1) * (y2 - y1)

print(round(abs(area), 3))
