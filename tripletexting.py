'''
1.7
https://open.kattis.com/problems/tripletexting
'''
s = input()

hashmap = {}
res = ''

for start in range(0, len(s), len(s) // 3):
    word = s[start: start + len(s) // 3]
    
    if word not in hashmap:
        hashmap[word] = 1
    else:
        hashmap[word] += 1

for k in hashmap.keys():
    if hashmap[k] > 1:
        print(k)