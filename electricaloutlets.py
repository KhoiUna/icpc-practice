'''
1.4
https://open.kattis.com/problems/electricaloutlets?tab=metadata
'''

for _ in range(int(input())):
    test_case =  [int(i) for i in input().split()]
    print(sum(test_case[1:]) - (test_case[0] - 1))