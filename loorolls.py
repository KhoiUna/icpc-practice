'''
1.7
https://open.kattis.com/problems/loorolls
'''

l,n = map(int, input().split())

remain = l % n
k = 1

while remain != 0:
    n -= remain
    remain = l % n
    k += 1

print(k)