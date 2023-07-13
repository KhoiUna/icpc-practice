'''
1.7
https://open.kattis.com/problems/kitten
'''
branches = []

branch = input()
start = branch

while branch != '-1':
    branch = input()
    branches.append(branch.split())

cache=[]
res = start
while start:
    count = 0
    for i, br in enumerate(branches):
        if start in br and i not in cache:
            start = br[0]
            res += ' ' + start
            cache.append(i)
            break

        count += 1

    if count == len(branches):
        start = None

print(res)