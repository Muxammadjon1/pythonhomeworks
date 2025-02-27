import json
import random
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(100000, 999999))
        while account_number in self.accounts:
            account_number = str(random.randint(100000, 999999))
        
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}")

    def view_account(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print("Error: Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number].balance += amount
                self.save_to_file()
                print(f"Deposit successful! New balance: ${self.accounts[account_number].balance:.2f}")
            else:
                print("Error: Deposit amount must be positive.")
        else:
            print("Error: Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if 0 < amount <= self.accounts[account_number].balance:
                self.accounts[account_number].balance -= amount
                self.save_to_file()
                print(f"Withdrawal successful! New balance: ${self.accounts[account_number].balance:.2f}")
            else:
                print("Error: Insufficient funds or invalid amount.")
        else:
            print("Error: Account not found.")

    def save_to_file(self):
        with open("accounts.json", "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)

    def load_from_file(self):
        if os.path.exists("accounts.json"):
            with open("accounts.json", "r") as file:
                try:
                    data = json.load(file)
                    for acc, details in data.items():
                        self.accounts[acc] = Account(details['account_number'], details['name'], details['balance'])
                except json.JSONDecodeError:
                    print("Error: Corrupted file or empty data.")