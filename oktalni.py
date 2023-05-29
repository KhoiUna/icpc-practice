'''
2.0
https://open.kattis.com/problems/oktalni?tab=metadata
'''
bin_str = input()

while len(bin_str) % 3 != 0:
    bin_str = '0' + bin_str

out = ''
for i in range(0, len(bin_str), 3):
    if bin_str[i:i+3] == '000':
        out += '0'
    if bin_str[i:i+3] == '001':
        out += '1'
    if bin_str[i:i+3] == '010':
        out += '2'
    if bin_str[i:i+3] == '011':
        out += '3'
    if bin_str[i:i+3] == '100':
        out += '4'
    if bin_str[i:i+3] == '101':
        out += '5'
    if bin_str[i:i+3] == '110':
        out += '6'
    if bin_str[i:i+3] == '111':
        out += '7'

print(out)
