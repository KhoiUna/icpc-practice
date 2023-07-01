'''
1.7
https://open.kattis.com/problems/titlecost
'''

[title, cost] = input().split()

cost = float(cost)

res = min(len(title), cost)
print(res)