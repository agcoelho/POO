

def create_acc(number, owner, balance, limit):
    acc = {'number': number, 'owner': owner, 'balance': balance, 'limit': limit}
    return acc


def deposit(acc, value):
    acc['balance'] += value

def withdraw(acc, value):
    acc['balance'] -= value

def extract(acc):
    print('You have ${:.2f}'.format(acc['balance']))