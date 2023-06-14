'''
1.4
https://open.kattis.com/problems/stopwatch?tab=metadata
'''

def main():
    n = int(input())

    diff = 0
    for i in range(n):
        time = int(input())
        diff = time - diff

    if n % 2 != 0: return 'still running'
    return diff
        
print(main())