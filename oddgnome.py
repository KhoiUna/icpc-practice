'''
1.7
https://open.kattis.com/problems/oddgnome?tab=metadata
'''

for _ in range(int(input())):
    gnomes = [int(i) for i in input().split()][1:]
    prev = gnomes[0]

    for i in range(1, len(gnomes)):
        if gnomes[i] - prev != 1:
            print(i+1)
            break

        prev = gnomes[i]