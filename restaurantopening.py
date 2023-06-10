'''
1.8
https://open.kattis.com/problems/restaurantopening?tab=metadata
'''

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    people = [int(i) for i in input().split()]
    matrix.append(people)


costs = []

for x in range(n):
    for y in range(m):
        current_location = [x, y]
        cost = 0

        for row_i in range(n):
            for col_i in range(m):
                num_of_ppl = matrix[row_i][col_i]
                distance_cost = abs(row_i - current_location[0]) + abs(col_i - current_location[1])
                cost += num_of_ppl * distance_cost

        costs.append(cost)

print(min(costs))