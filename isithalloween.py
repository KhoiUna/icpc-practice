'''
1.4
https://open.kattis.com/problems/isithalloween
'''

[d, n] = input().split()

if (d == 'OCT' and n == '31') or (d=='DEC' and n == '25'):
    print('yup')
else:
    print('nope')