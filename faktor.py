'''
1.3
https://open.kattis.com/problems/faktor
'''
import math

a, i = map(int, input().split())

out = a * i
while math.ceil(out / a) == i:
    out -= 1

print(out+1)