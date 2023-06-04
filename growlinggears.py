'''
2.0
https://open.kattis.com/problems/growlinggears?tab=metadata
'''
out = []
for _ in range(int(input())):
    T_max = 0
    gear_max = 0
    for i in range(int(input())):
        a, b, c = map(int, input().split())

        # dy/dx = 0 = -2aR + b
        # R = b/2a
        R = b / (2*a)

        T = -a * R**2 + b * R + c
        if T > T_max:
            T_max = T
            gear_max = i + 1

    out.append(gear_max)

for i in out:
    print(i)
