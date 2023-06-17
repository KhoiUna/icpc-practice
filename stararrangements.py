'''
1.7
https://open.kattis.com/problems/stararrangements
'''
s = int(input())
x,y = 2,1

print(str(s)+ ':')

while x + y <= s:    
    num_rows_for_y = s // (x + y)    
    num_stars_for_y = num_rows_for_y * y
    
    num_stars_for_x = s - num_stars_for_y

    is_valid = num_stars_for_x % x == 0
    
    if is_valid:
        print(str(x) +','+ str(y))

    y += 1

    if y > x:
        x += 1
        y -= 1