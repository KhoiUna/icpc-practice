# https://open.kattis.com/problems/commercials
# 1.8

# From wiki (https://en.wikipedia.org/wiki/Maximum_subarray_problem)
def max_sub_array(A):
    max_ending = 0
    max_so_far = 0
    
    for i in A:
        max_ending = max(0, max_ending + i)
        max_so_far = max(max_ending, max_so_far)        

    return max_so_far

[n,p] = input().split(' ')
n = int(n)
p = int(p)

A = [int(i) - p for i in input().split(' ')]
print(max_sub_array(A))