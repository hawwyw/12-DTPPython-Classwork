import time
user = "Bob"
account_balance = 1200
run = 1

def deposit(account_balance, deposit_amount):
    account_balance += deposit_amount
    print("Account balance updated")
    return account_balance

def withdraw(account_balance, withdraw_amount):
    if account_balance < withdraw_amount:
        print("Error - Insufficient Funds.")
    else:
        account_balance -= withdraw_amount
        print("Account balance updated")
    return account_balance

def check_balance(account_balance):
    print(f"${account_balance}")

def end():
    print("Thanks for using this program! :)")
    time.sleep(1.5)
    run = 2
    return run




while run == 1:
    func = int(input("If you want to deposit enter 1, withdraw 2, check balance 3, quit 4: "))
    if func == 1:
        deposit_amount = int(input("How much: "))
        account_balance = deposit(account_balance, deposit_amount)
    elif func == 2:
        withdraw_amount = int(input("How much: "))
        account_balance = withdraw(account_balance, withdraw_amount)
    elif func == 3:
        check_balance(account_balance)
    else:
        run = end()
