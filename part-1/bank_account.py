class BankAccount:
    def __init__(self, account_number:str, holder_name:str, balance:float=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount:float):
        if amount <= 0:
            return "Withdraw amount must be positive."
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"

    def check_balance(self):
        return self.balance

    def display_details(self):
        print("----- Bank Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : ${self.balance}")