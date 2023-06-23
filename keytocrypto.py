'''
1.7
https://open.kattis.com/problems/keytocrypto?tab=metadata
'''

cipher = input()
key = input()

plain = ''

for i in range(len(cipher)):
    cipher_ord = ord(cipher[i])  - ord('A')
    key_ord = ord(key[i]) - ord('A')

    plain_ord = ord('A') + (cipher_ord - key_ord) % 26
    plain_char = chr(plain_ord)

    plain += plain_char
    key += plain_char

print(plain)
