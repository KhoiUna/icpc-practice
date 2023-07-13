'''
1.7
https://open.kattis.com/problems/jewelrybox
'''
def calc(x,y,h):
    a = x - 2*h
    b = y - 2*h
    return a * b * h

for _ in range(int(input())):
    x,y = map(int, input().split())
    
    threshold = 10e-6
    lo = threshold
    hi = max(x, y) / 2

    while abs(hi - lo) > threshold:
        mid1 = lo + (hi - lo) * 1/3
        mid2 = lo + (hi - lo) * 2/3

        if calc(x, y, mid1) < calc(x, y, mid2):
            lo = mid1
        else:
            hi = mid2

    print(calc(x, y, hi))