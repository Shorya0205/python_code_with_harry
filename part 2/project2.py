#we are going to write a programm that generate a random no. and asks user to guess it 
#if the guess is wrong, it will tell the user whether the guess is too high or too low
#when the user guesses the correct number, it will congratulate them and tell how much attempts it took
import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Run the game

guess_the_number()
