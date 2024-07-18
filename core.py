class acc:
    def __init__(self, number, name, balance, limit):
        self.__number = number
        self.__name = name
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print('You have ${:.2f} available in your account for withdraw and ${:.2f} available in credit'.format(self.__balance, self.__limit))

    def withdraw(self):
        value = float(input('How much do you wish do withdraw?\n'))

        self.__balance -= value

        print('You still have ${:.2f} available'.format(self.__balance))

    def deposit(self):
        value = float(input('how much do you wish to deposit?\n'))

        self.__balance += value

        print('you now have {:.2f} available in your account'.format(self.__balance))