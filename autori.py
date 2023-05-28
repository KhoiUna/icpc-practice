'''
Difficulty: 1.2
https://open.kattis.com/problems/autori
'''

word = input().split('-')
out = ''
for w in word:
    out += w[0]
print(out)