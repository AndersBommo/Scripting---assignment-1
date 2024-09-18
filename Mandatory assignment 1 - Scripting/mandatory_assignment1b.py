# BACKACCOUNT 

class BankAccount: 
    def __init__(self, account_holder,  initial_balance=0) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance
       
    def deposit(self,amount): 
        self.balance += amount
    
    def withdraw(self,amount): 
        if amount <= self.balance: 
            self.balance -= amount
        else: 
            print("insuffienct funds")
    
    def account_info(self): 
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate=0.02, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied at {self.interest_rate * 100:.2f}%. New balance: ${self.balance:.2f}")

# Derived class for CheckingAccount with transaction fees
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, transaction_fee=1.0, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.balance:
            self.balance -= total_amount
            print(f"Withdrew ${amount:.2f} + ${self.transaction_fee:.2f} fee. New balance: ${self.balance:.2f}")
        else:
            print(f"Insufficient funds. Transaction fee of ${self.transaction_fee:.2f} included.")


