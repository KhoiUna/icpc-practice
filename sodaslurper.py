'''
1.7
https://open.kattis.com/problems/sodaslurper
'''

e,f,c = map(int, input().split())

total_empty = e + f

res = 0 

while total_empty >= c:
    consume = total_empty // c
    res += consume

    total_empty %= c
    total_empty += consume


print(res)