'''
1.4
https://open.kattis.com/problems/detaileddifferences
'''
ins = []
for _ in range(int(input())):
    ins.append([input(), input()])

for case in ins:
    res = ''
    for i in range(len(case[0])):
        if case[0][i] == case[1][i]: res += '.'
        else: res += '*'
    
    print(case[0])
    print(case[1])
    print(res)
    print()