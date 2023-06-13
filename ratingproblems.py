'''
1.4
https://open.kattis.com/problems/ratingproblems
'''

n,k = map(int, input().split())

total = sum([int(input()) for i in range(k)])


print((total - 3*(n-k)) / n, (total + 3*(n-k)) / n)