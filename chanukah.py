'''
1.4
https://open.kattis.com/problems/chanukah
'''

res = []

for _ in range(int(input())):
    _, n = map(int, input().split())
    res.append(sum([i for i in range(1, n+1)]) + n)
    
[print(i+1, res[i]) for i in range(len(res))]