'''
1.6
https://open.kattis.com/problems/prsteni
'''

# Find Greate Common Divisor using Euclidean algorithm
def gcd(a,b):
    r = a % b
    while r > 0:
        a, b = b, r
        r = a % b

    return b


_ = int(input())
rings = [int(i) for i in input().split()]

first = rings[0]

for ring in rings[1:]:
    divisor = gcd(first, ring)    
    print(str(first // divisor) + '/' + str(ring // divisor))