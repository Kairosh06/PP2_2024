class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print(f"Insufficient funds. Withdrawal failed. Current balance: ${self.balance}")

# Example:
account = BankAccount("Nurlan", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800) 