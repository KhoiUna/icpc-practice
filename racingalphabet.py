'''
1.6
https://open.kattis.com/problems/racingalphabet

Input
- Diameter 60 ft
- Speed: 15 ft per second btwn stops for pickups
- Each pickup is 1 second

Output:
- For each aphorism give the time for a smart player to complete the task
'''
import math
import string

alphabet_circle = list(string.ascii_lowercase + " '")

SPEED = 15
DIAMETER = 60
CIRCUMFERENCE_EACH_SLICE = DIAMETER * math.pi / 28

for _ in range(int(input())):
    aphorism = input().lower()
    current_index = alphabet_circle.index(aphorism[0])
    
    total_distance_run = 0
    pickup_time = 0

    for letter in aphorism:
        target_index = alphabet_circle.index(letter)

        distance = abs(current_index - target_index)
        '''
        If distance > 28 / 2
        then go another direction: 28 - distance
        '''
        if distance > 14:
            distance = 28 - distance

        total_distance_run += distance * CIRCUMFERENCE_EACH_SLICE

        # Move to target
        current_index = target_index
        pickup_time += 1

    print(total_distance_run / SPEED + pickup_time)