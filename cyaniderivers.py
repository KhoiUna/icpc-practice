'''
2.2
https://open.kattis.com/problems/cyaniderivers

Input:
- The first and the last tower in the row are always 1s.
- Towers standing in a river are represented by 0s, and the remaining towers are represented by 1s.
The order of the digits is the same as the order of towers in the row.
- 1s can be certified immediately. 
- The certification process of 0s takes one whole day. 
- 0s can be certified only if at least one of its immediate neighbour towers has been certified at least 1 day earlier.

Output: Minimum number of whole days in which all towers can be certified.
'''
import math

river_towers = input().split('1')

if not river_towers:
    print(0)
else:
    longest_sequence_streak = max(len(seq) for seq in river_towers)
    print(math.ceil(longest_sequence_streak / 2))