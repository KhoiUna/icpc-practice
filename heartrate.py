'''
1.4
https://open.kattis.com/problems/heartrate?tab=metadata
'''

for _ in range(int(input())):
    b, p = map(float, input().split())

    cal = round(60 * b / p,4)
    min = round(cal - 60 / p,4)
    max = round(cal + 60 / p,4)

    print(min, cal, max)