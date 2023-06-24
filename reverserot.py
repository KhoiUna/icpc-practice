'''
1.7
https://open.kattis.com/problems/reverserot
'''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
length = len(alphabet)

str = input()

while str != '0':
    [n, s] = str.split()
    n = int(n)
    s = [s[i] for i in range(len(s)-1, -1, -1)]

    res = []

    for c in s:
        idx = ord(c) - ord('A') + n

        if c == '_': idx = 26 + n
        elif c == '.': idx = 27 + n

        if idx >= length: idx -= length

        res.append(alphabet[idx])
    
    print(''.join(res))

    str = input()
