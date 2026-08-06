# bank sim

account = []
history = []
deposit = 0
def menu():
    print("1. Create account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Check balance.")
    print("5. History.")
    print("6. Exit")

def create_account():
        name = input("Enter your name: ")
        occupation = input("Enter your occupation: ")
        balance = int(input("Enter your balance: "))

        account.append({"name": name, "occupation": occupation, "balance": balance})


def deposit():
     user_name = input("Enter your name: ")
     for customer in account:
         if user_name.lower() == customer['name'].lower():
          deposit_amount = int(input("Enter your deposit amount: "))
          customer["balance"] += deposit_amount
          print("Your deposit amount is: ", deposit_amount)
          print("Your balance is: ", customer['balance'])
          transaction = (customer['name'] , "deposited :", deposit_amount)
          history.append(transaction)
          return

     else:
         print("Please enter a valid name")

def withdraw():
    user_name = input("Enter your name: ")
    for customer in account:
        if user_name.lower() == customer['name'].lower():
          withdraw_amount = int(input("Enter amount to withdraw :"))
          customer['balance'] -= withdraw_amount
          print("Withdraw amount: ", withdraw_amount)
          print("Your account balance: ", customer['balance'])
          transaction = ( customer['name'] ,"withdrew :  ", withdraw_amount )
          history.append(transaction)
          return
    else:
        print("Please enter a valid name")

def check_balance():
    user_name = input("Enter your name: ")
    for customer in account:
        if user_name.lower() == customer['name'].lower():
         print("Your account balance:  ",  customer['balance'])
         return
    else:
        print("Please enter a valid name")

def transaction_history():
    print("Transaction History:")
    for transaction in history:
        print(transaction)


print("Welcome to the MONEY LAUNDRY")

choice = 0
menu()
while choice != 6:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        transaction_history()
    else:
        print("Please enter a valid choice")
if choice == 6:
    print("Thank you for using MONEY LAUNDRY")
