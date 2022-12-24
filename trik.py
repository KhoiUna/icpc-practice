# https://open.kattis.com/problems/trik
'''
- ball under the leftmost cup.

Input:
  - move_string 
  
Output:
  - integer position
'''

move_string = input()

cups = [0, 1, 1]  # 0 is the ball in the leftmost cup

for move in move_string:
  if move == 'A':
    temp = cups[0]
    cups[0] = cups[1]
    cups[1] = temp

  if move == 'B':
    temp = cups[1]
    cups[1] = cups[2]
    cups[2] = temp

  if move == 'C':
    temp = cups[2]
    cups[2] = cups[0]
    cups[0] = temp

position = 0
while cups[position] != 0:
  position += 1

print(position + 1)
