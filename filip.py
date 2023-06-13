'''
1.3
https://open.kattis.com/problems/filip
'''

a,b = [''.join(reversed(list(i))) for i in input().split()]

print(max(a,b))