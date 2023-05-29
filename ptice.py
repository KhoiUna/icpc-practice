'''
1.6
https://open.kattis.com/problems/ptice
'''
adrian = 'abc' * 30
bruno = 'babc' * 30
goran = 'ccaabb' * 30
score = [['Adrian', 0], ['Bruno', 0], ['Goran', 0]]

input()
correct = input().lower()

for i in range(len(correct)):
    if adrian[i] == correct[i]:
        score[0][1] += 1
    if bruno[i] == correct[i]:
        score[1][1] += 1
    if goran[i] == correct[i]:
        score[2][1] += 1

highest = 0

for i in score:
    if i[1] > highest:
        highest = i[1]
print(highest)

name = ''
for i in score:
    if i[1] == highest:
        name += i[0] + '\n'
print(name)
