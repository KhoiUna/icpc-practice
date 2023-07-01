'''
1.7
https://open.kattis.com/problems/luhnchecksum
'''

for _ in range(int(input())):
    n = [int(i) for i in list(input())]

    for i in range(len(n)-2, -1, -2):
        n[i] *= 2

        if n[i] > 9:                
            n[i] = sum([int(i) for i in list(str(n[i]))])

    luhn_out = sum(n)

    if luhn_out % 10 == 0: print('PASS')
    else: print('FAIL')