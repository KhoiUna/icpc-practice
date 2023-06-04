'''
1.9
https://open.kattis.com/problems/overdraft?tab=metadata
'''
min_fee = 0
balance = 0

for _ in range(int(input())):
    transaction = int(input())

    if transaction < 0 and transaction + balance < 0:
        min_fee = min(transaction + balance, min_fee)

    balance += transaction


print(abs(min_fee))
