'''
1.4
https://open.kattis.com/problems/undeadoralive
'''

def main():
    line = input()

    if ":)" in line and ":(" in line: return 'double agent'
    
    if ":)" in line: return 'alive'
    
    if ":(" in line: return 'undead'

    return 'machine'


print(main())