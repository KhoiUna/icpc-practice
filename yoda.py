'''
2.1
https://open.kattis.com/problems/yoda?tab=metadata
'''

a = input()
b = input()

shorter_len = min(len(a), len(b))

f = ''
s = ''

for i in range(1, shorter_len+1):
    if int(a[-i]) > int(b[-i]):
        f = str(a[-i]) + f
    elif int(a[-i]) < int(b[-i]):
        s = str(b[-i]) + s
    else:
        f = str(a[-i]) + f
        s = str(a[-i]) + s


if len(a) > shorter_len:
    f = a[:len(a) - shorter_len] + f
if len(b) > shorter_len:
    s = b[:len(b) - shorter_len] + s

if len(f) == 0:
    print('YODA')
else:
    print(int(f))

if len(s) == 0:
    print('YODA')
else:
    print(int(s))
