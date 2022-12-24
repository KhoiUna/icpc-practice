# https://open.kattis.com/problems/pieceofcake2
'''
- each cake is 4cm thick

Input:
  - side horizontal vertical

Output:
  - volume of largest of 4 pieces after cuts 
'''

input = input()
[side, horizontal, vertical] = [int(number) for number in input.split(" ")]

thick = 4

horizontal_cut = side - horizontal
vertical_cut = side - vertical

first_volume = horizontal * vertical * thick
second_volume = horizontal_cut * vertical * thick
third_volume = horizontal_cut * vertical_cut * thick
fourth_volume = horizontal * vertical_cut * thick

volume = [first_volume, second_volume, third_volume, fourth_volume]
print(max(volume))