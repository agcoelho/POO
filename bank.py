import core
from core import login

account = core.Acc(1, 'baby', 2500, 6000, 0)
account2 = core.Acc(2, 'lice', 4000, 1200, 0)

core.login()

opt = False
while not opt:

    option = int(input('which operation do you choose?\n1-Trafer\n2-deposit\n3-withdraw\n4-see extract\n5-exit\n'))

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
        print('thankyou for choosing us! see you soon')
        


