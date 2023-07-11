'''
1.7
https://open.kattis.com/problems/lineup
'''

names = [input() for _ in range(int(input()))]

# set initial state
increasing = names[0] < names[1]
decreasing = not increasing

for i in range(1, len(names)):
    if i == len(names) - 1: break
    curr,next = names[i], names[i+1]

    if curr < next:
        increasing = True
    if curr > next:
        decreasing = True
 

if increasing and not decreasing:
    print('INCREASING')
elif decreasing and not increasing:
    print('DECREASING')
elif increasing and decreasing:
    print('NEITHER')