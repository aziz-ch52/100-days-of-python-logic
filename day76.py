# Program: Bank Account Class Implementation

# Step 1: Define the BankAccount class
class BankAccount:

    # Step 2: Constructor to initialize account details
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    # Step 3: Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Step 4: Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    # Step 5: Method to check current balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Step 6: Create an account object
name = input("Enter account holder name: ")
initial = float(input("Enter initial balance: "))

account = BankAccount(name, initial)

# Step 7: Perform operations
while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# End of Program
