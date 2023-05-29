'''
1.6
https://open.kattis.com/problems/server
'''
[_, t] = [int(i) for i in input().split(' ')]

count = 0
sum = 0
for i in input().split(' '):
    i = int(i)
    if t - sum < i:
        break

    sum += i
    count += 1

print(count)
