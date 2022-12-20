# https://open.kattis.com/problems/dicecup

user_input = input()

n = int(user_input.split(" ")[0])
m = int(user_input.split(" ")[1])

hash = {}

for i in range(1, n + 1):
    for j in range(1, m + 1):
        key = i + j
        if key in hash:
            hash[key] += 1
        else:
            hash[key] = 0


max = -1
for key in hash:
    if hash[key] > max:
        max = hash[key]

result = ''
for key in hash:
    if max == hash[key]:
        result += str(key) + '\n'

print(result)