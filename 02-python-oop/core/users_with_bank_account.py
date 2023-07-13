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
            #print(bank_account.display_account_info())
            print(f"balance : {bank_account.balance} interest : {bank_account.int_rate}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {"zibe3-bank" : BankAccount(int_rate=0.02, balance=0) , "zarafa-bank" : BankAccount(int_rate=0.02, balance=0)}
    
    
    def make_deposit(self, amount,account_name):
        self.accounts[account_name].deposit(amount)
        return self 
    
    def make_withdraw(self,amount,account_name):
        self.accounts[account_name].withdraw(amount)
        return self
    
    def display_user_balance(self,account_name):
        self.accounts[account_name].display_account_info()
        return self
    def transfer_money(self, amount, other_user ,account_name):
        self.make_withdraw(amount,account_name)
        other_user.make_deposit(amount,account_name)
        return self

    

goku = User("Goku","Songoku@sayan.xyz")
vegeta = User("Vegeta" ,"Vegeta@sayan.xyz")

goku.display_user_balance("zibe3-bank").make_deposit(120,"zibe3-bank").make_withdraw(10,"zibe3-bank").display_user_balance("zibe3-bank")

goku.transfer_money(20,vegeta,"zibe3-bank").display_user_balance("zibe3-bank")

vegeta.display_user_balance("zibe3-bank")



