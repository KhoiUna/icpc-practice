'''
1.4
https://open.kattis.com/problems/avion?tab=metadata
'''

res = ''

for i in range(5):
    if 'FBI' in input(): res += str(i+1) + ' '

if len(res) == 0: print('HE GOT AWAY!')
else: print(res)