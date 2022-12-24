# https://open.kattis.com/problems/acm

'''
Input:
- n lines of log entry:
  - int m an uppercase letter right|wrong

Output:
- 2 int on a single line
  - # problems solved total time measure
'''

log = input()

penalty = 0

right_log_hash = {}
wrong_log_hash = {}
total_time = 0

while log != '-1':
  [m, letter, rw] = log.split(' ')

  if rw == 'right':
    if not letter in right_log_hash:
      right_log_hash[letter] = int(m)
  else:
    if not letter in wrong_log_hash:
      wrong_log_hash[letter] = 1
    else:
      wrong_log_hash[letter] += 1

  log = input()

for key in wrong_log_hash:
  if key in right_log_hash:
    total_time += 20 * wrong_log_hash[key]

for key in right_log_hash:
  total_time += right_log_hash[key]

print(len(right_log_hash), total_time)
