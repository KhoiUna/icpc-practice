'''
1.4
https://open.kattis.com/problems/cetvrta
'''

x = {}
y = {}

for _ in range(3):
    l,r = map(int, input().split())

    if l in x: x[l] += 1
    else: x[l] = 1
    
    if r in y: y[r] += 1
    else: y[r] = 1

res = ''
for k in x.keys():
    if x[k] != 2: res += str(k) + ' '

for k in y.keys():
    if y[k] != 2: res += str(k) 

print(res)