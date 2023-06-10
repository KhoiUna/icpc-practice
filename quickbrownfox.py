'''
1.8
https://open.kattis.com/problems/quickbrownfox?tab=metadata
'''
from string import ascii_lowercase

ignore = [".", ",", "?", "!", "'", '"', " "]
          
n = int(input())
for _ in range(n):
    alphabet = list(ascii_lowercase)
    sentence = input().lower()
    missing = []

    for char in sentence:
        if char in ignore:
            continue

        if char in alphabet:
            alphabet.remove(char)

    if len(alphabet) == 0:
        print('pangram')
    else:
        print('missing', ''.join(alphabet))
