'''
1.7
https://open.kattis.com/problems/squarepeg

Square fits in a circle -> fits
'''
l,r = map(int, input().split())

area_of_largest_square = 2 * r**2

if area_of_largest_square >= l**2: print('fits')
else: print('nope')

'''
The largest square that could fit a circle has length of x:
    x^2 + x^2 = (2r)^2 (where r: radius of the circle -> its diagonal length is equal to 2r)
    -> 2x^2 = 4r^2
    -> x^2 = 2r^2 -> x = sqrt(2r^2)
    -> Area of the square: x^2 = 2r^2
'''