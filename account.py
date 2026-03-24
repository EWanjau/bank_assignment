class Account():

    def __init__(self, name, amount=10000):
        self.name = name
        self.amount = amount

    def check_balance(self):
        return self.amount

    def deposit_amount(self, deposit):
        self.amount += deposit
        return self.amount

    def withdraw_amount(self, withdraw):
        self.amount -= withdraw
        return self.amount