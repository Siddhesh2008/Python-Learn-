#Python Slot Machine Game
import random

def spin_row():
    symbols=["🍒", "🍋", "🔔", "🍉", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("---------------------------")
    print(" ".join(row))
    print("---------------------------")

def get_payout(row, bet):

    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100

    print("***********(Welcome to the Slot Machine Game!)***********")
    print(f"Your starting balance is: $ {balance:.2f}")
    print("symbols: 🍒, 🍋, 🍊, 🍉, ⭐")
    print("-------------------------------------------")

    while balance > 0:
        print(f"Current balance: $ {balance:.2f}")
        
        bet_input = input("Place your bet Amount: $")

        if not bet_input.isdigit():
            print("Invalid input. Please enter a valid whole number.")
            continue

        bet = int(bet_input)

        if bet > balance:
            print("Insufficient balance. Please place a lower bet.")
            continue
        if bet <= 0:
            print("Invalid bet amount. Please place a positive bet.")
            continue

        balance-=bet
        row=spin_row()
        print("Spinning the slot machine...\n")
        print_row(row)

        payout= get_payout(row, bet)

        if payout>0:
            print(f"Congratulations! You won $ {payout:.2f}!")
            balance+=payout
        else:
            print("Sorry, you didn't win this time.")

        play_again=input("Do you want to play again? (y/n): ")
        if play_again.lower()!="y":
            break
    print("-------------------------------------------")
    print(f"Game Over! Your final balance is: $ {balance:.2f}")
    print("--------------------------------------------")

if __name__=="__main__":
    main()