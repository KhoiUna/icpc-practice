'''
1.7
https://open.kattis.com/problems/prva
'''
r,c = map(int, input().split())

matrix = []
for _ in range(r):
    matrix.append(list(input()))

res = []

# Search horizontally
for row_i in range(r):
    str = ''
    for col_i in range(c):
        if matrix[row_i][col_i] == '#':             
            if len(str) >= 2:
                res.append(str)
            str = ''
            continue

        str += matrix[row_i][col_i]

    if len(str) >= 2:
        res.append(str)


# Seach vertically
for col_i in range(c):
    str = ''
    for row_i in range(r):
        if matrix[row_i][col_i] == '#':             
            if len(str) >= 2:
                res.append(str)
            str = ''
            continue

        str += matrix[row_i][col_i]

    if len(str) >= 2:
        res.append(str)


print(sorted(res)[0])