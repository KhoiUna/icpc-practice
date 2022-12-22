# https://open.kattis.com/problems/pyramids

'''
write a program that computes how high a pyramid can be built 
given a certain number of blocks of stone.

- side length that is two less than the one below it
- The top layer always consist of a single block

Input:
    - int n : number of blocks

Output:    
    - int max_h : max height of a pyramid that can be built with at least n blocks.
'''

n = int(input())

max_h = 0

side_start = 1
while side_start**2 <= n:
    max_h += 1
    n -= side_start**2
    side_start += 2


print(max_h)