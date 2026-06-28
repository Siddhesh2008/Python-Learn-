import random

options=("rock","paper","scissor")

running=True
while running:
         player=None
         computer=random.choice(options)
         while player not in options:
            player=input("Enter a choice: ").lower()
            print(f"Player:  {player}")
            print(f"Computer: {computer}")

            if player==computer:
               print("It is a TIE!")
            elif player=="rock" and computer=="scissor":
               print("YOU WIN!!")
            elif player=="paper" and computer=="rock":
               print("YOU WIN!!")
            elif player=="scissor" and computer=="paper":
               
               print("YOU WIN!!")
            else:
               print("YOU LOSE!!!")
            
            play_again=input("Play again? (y/n)").lower()
            if not play_again=="y":
                  running= False
                    
                    

print("thanks!!")
