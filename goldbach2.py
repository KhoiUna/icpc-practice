'''
2.2
https://open.kattis.com/problems/goldbach2
'''


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2

    while p**2 <= n:
        if prime[p]:
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1

    return prime


n = int(input())
is_prime = sieve_of_eratosthenes(32000)

for i in range(n):
    target = int(input())

    representations = []
    for i in range(2, int(target / 2) + 1):
        first = i
        second = target - i
        if is_prime[first] and is_prime[second]:
            representations.append(str(first) + '+' + str(second))

    print(target, 'has', len(representations), 'representation(s)')
    for r in representations:
        print(r)
    print()
