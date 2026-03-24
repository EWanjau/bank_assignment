class Account():

    def __init__(self, name, amount=10000):
        self.name = name
        self.amount = amount

    def check_balance(self):
        return self.amount

    def deposit_amount(self, deposit):
        if deposit <= 0:
            print("Amount must be higher than Kshs 0")
        self.amount += deposit
        return self.amount

    def withdraw_amount(self, withdraw):
        if withdraw <= 0:
            return print("Amount must be higher than Kshs 0")
        else:
            self.amount -= withdraw
            return self.amount