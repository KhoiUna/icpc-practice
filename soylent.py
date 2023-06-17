'''
1.7
https://open.kattis.com/problems/soylent
'''
import math

CALORIE_PER_BOTTLE = 400

n = int(input())
test_cases = [int(input()) for _ in range(n)]

for v in test_cases:
    print(math.ceil(v / CALORIE_PER_BOTTLE))