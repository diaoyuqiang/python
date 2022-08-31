class DepoBankProcess(object):

    def __init__(self):
        pass

    def deposite(self):
        print('deposite')


class WitBankProcess(object):

    def __init__(self):
        pass

    def withdraw(self):
        print('withdraw')


class Customer(object):
    def __init__(self, type):
        self.type = type


class Client(object):

    def __init__(self, customer):
        self.customer = customer
        self.bankprocess = None

    def process(self):

        if self.customer.type == 'deposite':
            self.bankprocess = DepoBankProcess()
            self.bankprocess.deposite()

        elif self.customer.type == 'withdraw':
            self.bankprocess = WitBankProcess()
            self.bankprocess.withdraw()
        else:
            pass


if __name__ == '__main__':
    customer = Customer('withdraw')
    client = Client(customer)
    client.process()
    customer.type = 'deposite'
    client.process()