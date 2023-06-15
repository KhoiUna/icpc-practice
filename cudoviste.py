'''
1.4
https://open.kattis.com/problems/cudoviste

Input:
- # building ; X parked car ; . free space
- Monster truck 2x2
- Cannot park on building

Output:
- number of possible parking spaces grouped by the number of cars he needs to squash to park in them,
    not the number of cars he will squash on the way over.
- 5 lines, the total number of parking spaces Mirko can park on if he squashes 
    0 cars (first line), 
    1 car (second line), 
    2 cars (third line), 
    3 cars (fourth line), 
    4 cars (fifth line).
'''

r,c = map(int, input().split())

matrix = [list(input()) for _ in range(r)]
res = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
}

for row_i in range(r):
    for col_i in range(c):
        if matrix[row_i][col_i] == '#': continue
        if row_i == r-1 or col_i == c-1: continue

        count_building = 0
        count_x = 0
        
        for i in range(row_i, row_i+2):
            for j in range(col_i, col_i+2):
                if matrix[i][j] == '#': 
                    count_building += 1
                    break

                if matrix[i][j] == 'X': count_x += 1

        if count_building == 0: res[count_x] += 1


[print(i) for i in res.values()]