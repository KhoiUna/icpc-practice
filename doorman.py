'''
2.2
https://open.kattis.com/problems/doorman?tab=metadata

- the club is full, the number of women and men let into the club should be roughly the same
- decide to let the second person in the queue cut the line and slip into the club before the person in front
'''

max_diff = int(input())
s = list(input())

m = 0
w = 0

while abs(w - m) <= max_diff and len(s) > 0:
    if len(s) > 1:
        '''
        Switch 1st and 2nd person if they are opposite gender
        and gender difference is larger than `max_diff`
        '''
        if (s[0] == 'W' and s[1] == 'M' and abs(w + 1 - m) > max_diff) or (s[0] == 'M' and s[1] == 'W' and abs(w - (m + 1)) > max_diff):  
            temp = s[0]
            s[0] = s[1]
            s[1] = temp
        
        # If 1st and 2nd person are same gender then `break` the while loop
        elif (s[0] == 'W' and s[1] == 'W' and abs(w + 1 - m) > max_diff) or (s[0] == 'M' and s[1] == 'M' and abs(w - (m + 1)) > max_diff):
            break

    # Let the 1st person in
    if s[0] == 'W':
        w += 1
    elif s[0] == 'M':
        m += 1
    s.pop(0)
    

print(m + w) # Print max number of people