'''
1.4
https://open.kattis.com/problems/everywhere
'''

for _ in range(int(input())):
    places = set()

    for _ in range(int(input())):
        places.add(input())

    print(len(places))