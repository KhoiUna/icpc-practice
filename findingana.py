'''
1.3
https://open.kattis.com/problems/findingana
'''

word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(word[i:])
        break