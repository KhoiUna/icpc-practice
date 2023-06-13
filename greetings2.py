'''
1.3
https://open.kattis.com/problems/greetings2
'''

count = 0
for char in input():
    if char  == 'e':
        count += 1

print('h'+'e'*count*2+'y')