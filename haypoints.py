'''
2.0
https://open.kattis.com/problems/haypoints?tab=metadata
'''
m,n = map(int, input().split())

hashmap = {}

points = ''

for _ in range(m):
    [w, dollar] = input().split()
    dollar = int(dollar)
    hashmap[w] = dollar

for _ in range(n):    
    curr = 0
    sentence = input()
    while sentence != '.':
        for word in sentence.split():
            if word in hashmap:
                curr += hashmap[word]

        sentence = input()
    
    points += str(curr) + '\n'

print(points)