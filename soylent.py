'''
1.7
https://open.kattis.com/problems/soylent
'''
CALORIE_PER_BOTTLE = 400

n = int(input())
test_cases = [int(input()) for _ in range(n)]

for v in test_cases:
    print(v // CALORIE_PER_BOTTLE)