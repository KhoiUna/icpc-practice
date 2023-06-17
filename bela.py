'''
1.4
https://open.kattis.com/problems/bela
'''

[n, dominant_suit] = input().split()
n = int(n)

point_map = {
    'A': {
        'dominant': 11,
        'not_dominant': 11,
    },
    'K': {
        'dominant': 4,
        'not_dominant': 4,
    },
    'Q': {
        'dominant': 3,
        'not_dominant': 3,
    },
    'J': {
        'dominant': 20,
        'not_dominant': 2,
    },
    'T': {
        'dominant': 10,
        'not_dominant': 10,
    },
    '9': {
        'dominant': 14,
        'not_dominant': 0,
    },
    '8': {
        'dominant': 0,
        'not_dominant': 0,
    },
    '7': {
        'dominant': 0,
        'not_dominant': 0,
    },
}

res = 0
for _ in range(4*n):
    card = input()

    if card[1] == dominant_suit: res += point_map[card[0]]['dominant']
    else: res += point_map[card[0]]['not_dominant']


print(res)