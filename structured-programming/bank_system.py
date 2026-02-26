# Simple Bank System - Structured Programming Example

accounts = {}

def create_account(account_number, owner):
    if account_number in accounts:
        print("Account already exists.")
        return
    accounts[account_number] = {
        "owner": owner,
        "balance": 0
    }
    print("Account created successfully.")

def deposit(account_number, amount):
    if account_number not in accounts:
        print("Account not found.")
        return
    accounts[account_number]["balance"] += amount
    print("Deposit successful.")

def withdraw(account_number, amount):
    if account_number not in accounts:
        print("Account not found.")
        return
    if accounts[account_number]["balance"] < amount:
        print("Insufficient funds.")
        return
    accounts[account_number]["balance"] -= amount
    print("Withdrawal successful.")

def show_balance(account_number):
    if account_number not in accounts:
        print("Account not found.")
        return
    print("Balance:", accounts[account_number]["balance"])

def menu():
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            acc = input("Account number: ")
            owner = input("Owner name: ")
            create_account(acc, owner)
        elif choice == "2":
            acc = input("Account number: ")
            amount = float(input("Amount: "))
            deposit(acc, amount)
        elif choice == "3":
            acc = input("Account number: ")
            amount = float(input("Amount: "))
            withdraw(acc, amount)
        elif choice == "4":
            acc = input("Account number: ")
            show_balance(acc)
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
