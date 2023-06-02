'''
1.8
https://open.kattis.com/problems/statistics?tab=metadata
'''
count = 1
while True:
    try:
        _, *test_case = list(map(int, input().split(' ')))
    except EOFError:
        break

    lowest = min(test_case)
    highest = max(test_case)
    diff = highest - lowest

    print("Case {}: {} {} {}".format(count, lowest, highest, diff))
    count += 1
