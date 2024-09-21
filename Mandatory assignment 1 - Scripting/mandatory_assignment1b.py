# Base class for BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=None):
        self.account_holder = account_holder
        self.balance = balance if balance is not None else 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds on your account")
        else:
            self.balance -= amount
            return self.balance

    def account_info(self):
        return f'Account holder: {self.account_holder}, Balance: ${self.balance:.2f}'


# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=None, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
        print(f"Interest applied at {self.interest_rate * 100:.2f}%. New balance: ${self.balance:.2f}")


# CheckingAccount subclass with transaction fee
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=None, transaction_fee=1.0):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total_withdrawal = amount + self.transaction_fee
        if self.balance < total_withdrawal:
            print("Insufficient funds in your checking account")
        else:
            super().withdraw(total_withdrawal)  
            print(f"Withdrew ${amount:.2f} + ${self.transaction_fee:.2f} fee. New balance: ${self.balance:.2f}")


### TEST 1 Savings Account
print("TEST 1 Savings Account\n")
AndersSavings = SavingsAccount('Anders Bommo', 100)
#depositing 10 and withdrawing 50 and Applying interest
print(AndersSavings.account_info())
AndersSavings.deposit(10)
print(AndersSavings.account_info())
AndersSavings.withdraw(100)
print(AndersSavings.account_info())
AndersSavings.withdraw(50)
print(AndersSavings.account_info())
AndersSavings.apply_interest()
print(AndersSavings.account_info())
print("\n")

### Test 2 Checkings Account
print("Test 2 Checkings Account\n")
AndersCheckings = CheckingAccount("Anders Bommo", 100)
#depositing 10 and withdrawing 110 and withdrawing 109
print(AndersCheckings.account_info())
AndersCheckings.deposit(10)
print(AndersCheckings.account_info())
AndersCheckings.withdraw(110)
print(AndersCheckings.account_info())
AndersCheckings.withdraw(109)
print(AndersCheckings.account_info())
print("\n")