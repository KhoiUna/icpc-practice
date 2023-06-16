'''
1.4
https://open.kattis.com/problems/bijele
'''

seq = [int(i) for i in input().split()]
arr = [1,1,2,2,2,8]

res = ''
for i in range(len(seq)):
    res += str(arr[i] - seq[i]) + ' '

print(res)