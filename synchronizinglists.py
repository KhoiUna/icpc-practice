'''
1.7
https://open.kattis.com/problems/synchronizinglists
'''
n = int(input())

while n != 0:
    original = [int(input()) for _ in range(n)]
    sorted_original = sorted(original)

    second = [int(input()) for _ in range(n)]
    second.sort()

    position = {}
    for i in range(n):
        if sorted_original[i] not in position: position[sorted_original[i]] = second[i]

    [print(position[value]) for value in original]
    print()

    n = int(input())
