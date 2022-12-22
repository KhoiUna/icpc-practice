# https://open.kattis.com/problems/pokechat

'''

Input:
    - string s
    - string id
'''

s = input()
id = input()

num = []

index = 0
while index < len(id):
    num.append(int(id[index: index + 3]))
    index += 3


poke_name = ''
for i in num:
    if i > len(s):
        continue
    
    poke_name += s[i - 1]

print(poke_name)