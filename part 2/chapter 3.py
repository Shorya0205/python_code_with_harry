#MORE QUESTIONS OF FILE I/O
#AGAME OF CHOOSING A RANDOM NUMBER IF YOUR OUTCOMEIS GREATER THAN HIGH SCORE THAN YOU WIN AND HIGH SCORE WILL BE UPDATED
import random
def play_game():
    print("Welcome to the High Score Game!")
    a=input("Press Enter to continue... OR EXIT TO LEAVE").lower()
    if a == "exit":
        print("Exiting the game. Goodbye!")
        return
    score =random.randint(1, 100)
    print(f"Your score is: {score}")
    with open("HIGHSCORE.txt", "r") as file:
        high_score = int(file.read())
    print(f"Current High Score: {high_score}")
    if score > high_score:
        print("Congratulations! You've set a new high score!")
        with open("HIGHSCORE.txt", "w") as file:
            file.write(str(score))
    else:
        print("You did not beat the high score. Better luck next time!")


# Run the game
play_game()
want_to_play_again = input("Do you want to play again? (yes/no): ").lower()
while want_to_play_again == "yes":
    play_game()
    want_to_play_again = input("Do you want to play again? (yes/no): ").lower()

    
