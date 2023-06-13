'''
1.4
https://open.kattis.com/problems/magictrick?tab=metadata
'''


def main():
    hashmap = {}
    
    for char in input():
        if char in hashmap:
            return 0

        hashmap[char] = 1

    return 1

print(main())