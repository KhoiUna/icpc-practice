'''
1.7
https://open.kattis.com/problems/schoolspirit?tab=metadata
'''
n = int(input())
scores = [int(input()) for _ in range(n)]

group_score = 0
for i in range(n):
    group_score += scores[i] * (4/5)**i

print(group_score * 1/5)

average = 0
for i in range(n):
    g = 0

    # We start counting from 0 when one leaves
    new_i = 0 

    for j in range(n):
        if j == i: continue

        g += scores[j] * (4/5)**new_i        
        new_i += 1

    average += g  * 1/5

print(average / n)