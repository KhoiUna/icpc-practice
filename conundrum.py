'''
1.4
https://open.kattis.com/problems/conundrum?tab=metadata
'''

s = input()

name = ['P', 'E', 'R']
days = 0

for i in range(len(s)):
    if s[i] != name[i % 3]: days+=1

print(days)