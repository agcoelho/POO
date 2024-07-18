import functions

acc = functions.create_acc(12, 'baby', 1600, 6000)

print(acc)


deposit = float(input('how much do you wish to deposit?\n'))

functions.deposit(acc, deposit)

functions.extract(acc)

withdraw = float(input('how much do you wish to withdraw?\n'))

functions.withdraw(acc, withdraw)

functions.extract(acc)

