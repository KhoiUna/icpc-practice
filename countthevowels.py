'''
1.3
https://open.kattis.com/problems/countthevowels?tab=metadata
'''

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for char in input().lower():
    if char in vowels: count += 1

print(count)