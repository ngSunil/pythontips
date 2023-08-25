# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 300
# D 300
# W 200
# D 100
# 500
lst = []
x = input()
while x != '':
    lst.append(x)
    x = input()
balance = 0
for x in lst:
    if x.startswith('D'):
        balance += int(x.strip('D '))
    elif x.startswith('W'):
        balance -= int(x.strip('W '))
print(balance)
