class Acc:
    def __init__(self, id, name, balance, limit, value):
        self.__id = id
        self.__name = name
        self.__balance = balance
        self.__limit = limit
        self.value = value

    def extract(self):
        print('You have ${:.2f} available in your account for withdraw and ${:.2f} available in credit'.format(self.__balance, self.__limit))

    def withdraw(self):
        self.value = float(input('How much do you wish do withdraw?\n'))

        self.__balance -= self.value

        print('You still have ${:.2f} available'.format(self.__balance))

    def deposit(self):
        self.value = float(input('how much do you wish to deposit?\n'))

        self.__balance += self.value

        print('you now have {:.2f} available in your account'.format(self.__balance))
        

    def transfer(self, destination):
        option = 0
        while option != 1:
            self.value = float(input('how much do you wish to transfer?\n'))

            print('transfer {:.2f} to {}'.format(self.value, destination))

            option = int(input('Is everything correct?\n1-YES\n2-NO\n'))
            if option == 1:
                self.__balance -= self.value
                destination.__balance += self.value
                print('congratulations! everything went well, your current balance is: {:.2f}'.format(self.__balance))
            

def login():
        print('####################################\n')
        print("     WELLCOME TO BABY'S BANK          ")
        print('####################################\n')

        user = '0'
        validation = False
        while not validation:
            user = input('type your username\n')
            if user == 'baby':
                pswd = input('type your password, baby\n')
                if pswd != '1234':
                    print('invalid password, baby\n')
                else: 
                    print('wellcome baby!!!\n')
                    validation = True
            elif user == 'lice':
                pswd = input('type your password, lice\n')
                if pswd != '4321':
                    print('invalid password\n')
                else: 
                    print('wellcome lice!!!\n')
                    validation = True
            else:
                print('invalid username or password, pls try again')
        