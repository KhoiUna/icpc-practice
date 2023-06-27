'''
1.7
https://open.kattis.com/problems/mjehuric
'''
seq = input().split()

while ' '.join(seq) != '1 2 3 4 5':
    for i in range(len(seq)-1):
        if int(seq[i]) > int(seq[i+1]):
            temp = seq[i]
            seq[i] = seq[i+1]
            seq[i+1] = temp

            print(' '.join(seq))