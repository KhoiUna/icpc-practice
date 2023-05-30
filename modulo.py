'''
1.6
https://open.kattis.com/problems/modulo
'''
set = set()

for i in range(10):
    set.add(int(input()) % 42)

print(len(set))
