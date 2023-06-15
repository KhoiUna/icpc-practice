'''
1.4
https://open.kattis.com/problems/cutthenegativity?tab=metadata
'''
n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(i) for i in input().split()])

count = 0
res = ''
for i in range(1,n+1):
    for j in range(1,n+1):
        cost = matrix[i-1][j-1]
        if cost > -1: 
            res += str(i) + ' ' + str(j) + ' ' + str(cost) + '\n'
            count += 1

print(count)
print(res)