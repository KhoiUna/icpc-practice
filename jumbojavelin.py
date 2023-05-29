'''
1.3
https://open.kattis.com/problems/jumbojavelin
'''
i = int(input())

out = 0
while i > 0:
    out += int(input()) - 1
    i -= 1

print(out + 1)
