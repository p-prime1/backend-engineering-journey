class BankAccount():
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount:int):
        self.balance -= amount

    def get_balance(self):
        return f"Current balance: {self.balance}"

prime_account = BankAccount("Prime", 1000)
print(prime_account.get_balance())
prime_account.deposit(100)
print(prime_account.get_balance())
prime_account.withdraw(50)
print(prime_account.get_balance())
