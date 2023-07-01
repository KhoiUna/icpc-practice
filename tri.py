'''
1.7
https://open.kattis.com/problems/tri
'''

x,y,z = [int(x) for x in input().split()]

if x+y==z:
    print(f"{x}+{y}={z}")
elif y+z==x:
    print(f"{x}={y}+{z}")
elif x-y==z:
    print(f"{x}-{y}={z}")
elif y-z==x:
    print(f"{x}={y}-{z}")
elif x*y==z:
    print(f"{x}*{y}={z}")
elif y*z==x:
    print(f"{x}={y}*{z}")
elif x/y==z:
    print(f"{x}/{y}={z}")
elif y/z==x:
    print(f"{x}={y}/{z}")
