'''
1.7
https://open.kattis.com/problems/tornbygge
'''

_ = int(input())
x = [int(i) for i in input().split()]

res = 1

for i in range(len(x)):
    if i == len(x) - 1:  break

    curr, next = x[i], x[i+1]

    if next > curr: res += 1

print(res)