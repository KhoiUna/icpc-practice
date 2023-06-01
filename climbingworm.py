'''
2.4
https://open.kattis.com/problems/climbingworm
'''
[a, b, h] = [int(i) for i in input().split(' ')]

count = 0
while h > 0:
    h -= a
    count += 1

    if h <= 0:
        break

    h += b

print(count)
