import core

account = core.Acc(2, 'baby', 4000, 6000, 0)
account2 = core.Acc(2, 'lice', 4000, 1200, 0)
#teste
core.login()

opt = False
while not opt:

    option = int(input('which operation do you choose?\n1-Transfer\n2-Deposit\n3-Withdraw\n4-See extract\n5-Exit\n'))

    if option == 1:
        account.transfer(account2)
    elif option == 2:
        account.deposit()

    elif option == 3:
        account.withdraw()

    elif option == 4:
        account.extract()

    else:
        opt = True
        print('thank you for choosing us! see you soon...')

print('o valor na conta agora é de: {:.2f}'.format(account2.get_balance))
        


