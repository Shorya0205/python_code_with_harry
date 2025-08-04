#  PROJECT NAME = STONE PAPER SCISSOR GAME
import random
count=0
list=["stone","paper","scissor"]

print("Welcome to the Stone Paper Scissor Game!")
while True:
 for i in range(3):
    print("Round", i + 1)
    
    computer=random.choice(list)
    
    print("You have 3 chances to win the game.")
    
    user=input("Enter your choice (stone, paper, scissor): ").lower()
    
    if(user not in list):
        print("Invalid choice! Please choose stone, paper, or scissor.")
        continue  
    elif((user=="stone" and computer=="scissor") or (user=="scissor" and computer=="paper") or( user=="paper" and computer=="stone")):
        print("You won this round!The computer has chosen",computer)
        count += 1
    elif(user==computer):
        print("It's a tie!")  
    else:
        print("You lose! The computer chose", computer)
      

    if count >= 2:
        print("Congratulations! You won the game with", count, "out of 3 rounds.")
    else:
        print("You lost the game. You won only", count, "out of 3 rounds.")
        print("Better luck next time!")
 decision = input("Do you want to play again? (yes/no): ").lower()
 if decision != "yes":
  print("Thank you for playing! Goodbye!")
  break
    