'''
2.0
https://open.kattis.com/problems/measurement?tab=metadata
'''
unit_conversion_in_thou = {
    'thou': 1,
    'inch': 1000,
    'foot': 12 * 1000,
    'yard': 3 * 12000,
    'chain': 22 * 3 * 12000,
    'furlong': 10 * 22 * 36000,
    'mile': 8 * 10 * 22 * 36000,
    'league': 3 * 8 * 10 * 22 * 36000
}
unit_conversion_in_thou_abbr = {
    'th': 1,
    'in': 1000,
    'ft': 12 * 1000,
    'yd': 3 * 12000,
    'ch': 22 * 3 * 12000,
    'fur': 10 * 22 * 36000,
    'mi': 8 * 10 * 22 * 36000,
    'lea': 3 * 8 * 10 * 22 * 36000
}

[v, from_u, _, to_u] = input().split(' ')
v = int(v)

if from_u in unit_conversion_in_thou:
    from_u = unit_conversion_in_thou[from_u]
if from_u in unit_conversion_in_thou_abbr:
    from_u = unit_conversion_in_thou_abbr[from_u]

if to_u in unit_conversion_in_thou:
    to_u = unit_conversion_in_thou[to_u]
if to_u in unit_conversion_in_thou_abbr:
    to_u = unit_conversion_in_thou_abbr[to_u]

print(v * from_u / to_u)
