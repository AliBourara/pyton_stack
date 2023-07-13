class BankAccount:
    all_instances =[]
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        

    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= self.int_rate
        return self
    
    @classmethod
    def bank_info(cls):
        for bank_account in cls.all_instances:
            bank_account.display_account_info()

        return None



goku = BankAccount(7,250)
vegeta = BankAccount(9,310)


goku.deposit(10).deposit(10).deposit(8).withdraw(120).yield_interest().display_account_info()
vegeta.deposit(15).deposit(12).withdraw(120).withdraw(105).withdraw(90).withdraw(60).yield_interest().display_account_info()


BankAccount.bank_info() 