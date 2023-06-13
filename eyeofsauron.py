'''
1.4
https://open.kattis.com/problems/eyeofsauron
'''
seq = input()

stop_i = 0
for i in range(len(seq)):
    if seq[i] == '(':
        stop_i = i
        break

if seq[:stop_i] == seq[stop_i+2:] and seq[stop_i+1] == ')': print('correct')
else: print('fix')