'''
1.4
https://open.kattis.com/problems/pet
'''

highest = 0
winner = 0

for i in range(1, 6):
    point = sum(map(int, input().split()))
    
    if point > highest:
        winner = i
        highest = point

print(winner, highest)