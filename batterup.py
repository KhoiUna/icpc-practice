'''
1.3
https://open.kattis.com/problems/batterup
'''

input()
line = [int(i) for i in input().split()]

total = 0
count = 0

for num in line:
    if num == -1:
        continue
    
    total += num
    count += 1

print(total / count)