#python banking program

def show_balance(balance):
    print(f"Your current balance is: $ {balance:.2f}")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"Deposit successful. Your new balance is: $ {balance:.2f}")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. Your new balance is: $ {balance:.2f}")
    else:
        print("Insufficient funds.")
    return balance
def main():
    balance=0
    is_running=True

    while is_running:
        print("------------------------")
        print("\nWelcome to the Bank!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance = deposit(balance, amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif choice == '4':
            print("Thank you for banking with us. Goodbye!")
            is_running = False
        else:
            print("-------------------------")
            print("Invalid option. Please try again.")
            print("-------------------------")

if __name__ == "__main__":
    main()