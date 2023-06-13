'''
1.4
https://open.kattis.com/problems/planina
'''


n = int(input())

print( (2**n + 1)**2 ) # Explanation for this formula below

'''
n=1 -> 9 points -> 3^2 points -> (2^1 + 1)^2 points

n=2 -> 25 points -> 5^2 points -> (2^2 + 1)^2 points
etc...

A pattern is seen.
'''