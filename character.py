'''
2.4
https://open.kattis.com/problems/character
'''

n = int(input())

'''
Formula for the subset is: 2**n
Minus n since we want the subset to have at least 2 characters
Minus 1 to remove the empty subset.
'''
print(2**n - n - 1)
