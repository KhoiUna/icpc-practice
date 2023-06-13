'''
1.3 - 1.4
https://open.kattis.com/problems/oddecho
'''

words = []
for _ in range(int(input())):
    words.append(input())

for i in range(len(words)):
    if i % 2 == 0:
        print(words[i])