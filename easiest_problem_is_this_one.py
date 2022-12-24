# https://open.kattis.com/problems/easiest
'''
Input:
  - multiple lines of input
  
Output:
  - p bigger than 10 (start from 11)
'''

input_array = []

num = int(input())
while num != 0:
  input_array.append(num)
  num = int(input())


def total_digits(number):
  number = str(number)

  total = 0
  for digit in number:
    total += int(digit)

  return total


p = 11
for number in input_array:
  while total_digits(p * number) != total_digits(number):
    p += 1

  print(p)
  p = 11
