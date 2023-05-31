'''
2.2
https://open.kattis.com/problems/eventplanning?tab=metadata
'''
n, b, h, _ = map(int, input().split())

# Ensure `min_cost` is bigger than `b` budget in the start
min_cost = b + 1

for _ in range(h):
    price = int(input())

    for bed in input().split(' '):
        bed = int(bed)
        if bed >= n:
            min_cost = min(min_cost, n * price)

if min_cost <= b:
    print(min_cost)
else:
    print('stay home')
