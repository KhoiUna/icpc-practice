# https://open.kattis.com/problems/whichisgreater

user_input = input()

first = int(user_input.split(" ")[0])
second = int(user_input.split(" ")[1])

if first > second:
    print(1)
else:
    print(0)
