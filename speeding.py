# https://open.kattis.com/problems/speeding
# Difficulty: 1.6
'''
Input:
  - first line: integer n -> max_photo
  - next line: t d -> separated w single space

Output: 
  - integer greatest speed
'''

max_photo = int(input())

speed_arr = []

count = 0
prev_t = 0
prev_d = 0
while count < max_photo:
  [t, d] = input().split(" ")
  t = int(t)
  d = int(d)

  if count == 0:
    prev_t = t
    prev_d = d
    count += 1
    continue

  speed = (d - prev_d) // (t - prev_t)
  speed_arr.append(speed)

  prev_t = t
  prev_d = d
  count += 1

print(max(speed_arr))
