'''
2.2
https://open.kattis.com/problems/marswindow?tab=metadata
'''
y = int(input())

upper_diff = ((y - 2018) * 12) + 9

if (upper_diff / 26 - upper_diff // 26) <= 12/26:
    print('yes')
else:
    print('no')

# EX: 2020: year difference in months = 24 months
# Because month starts in april, actual month difference + 8 + 1 = 33 months
    # + 1 because to include same month
# This includes the entire year, so the range of window is actually 32-12 to 32 months away
    # 20 to 32 months window

# Check if x number of complete cycles fall within this window
# 26 * x = 20 to 32
# Divide both sides by 20, x = 0.76 to 1.23
# Since x can only be an integer, x can be 1, so 2020 window is valid
# Note that the range is 32/26 - 20/26 = 12/26
    # So just need to check upper bound (i.e 33 months here)

# Because the difference can only be 12/26 or ~ 0.46 below the upper bound,
# take the floor division and check if the difference between the normal division
# and floor division is equal or below 0.46, because the lower bound must be below or equal to that
