# number guessing game lvl 2

import random
number = random.randint(1, 100)
user_guess = 0
attempts = 7
guesses = 0

def welcome():
    print(f"Welcome to the Number Guessing Game, BOZO!")
def play_game():
    global attempts, user_guess, guesses
    if user_guess > number:
        print("Too high!")
        attempts -= 1
        guesses += 1
        print(f'remaining attempts: {attempts}')
    elif user_guess < number:
        print("Too low!")
        attempts -= 1
        guesses += 1
        print(f'remaining attempts: {attempts}')
def win_game():
        print("You win! BOZO")
        print(f"You guessed it in {guesses} attempts!")
        return
def game_over():
    if attempts == 0 and user_guess != number:
      print(f"Game Over! the number was{number}")
def play_again():
    global attempts, user_guess,number, guesses
    number = random.randint(1, 100)
    attempts = 7
    user_guess = 0
    guesses = 0

    insert_coin = input("would you like to play again? :")
    if insert_coin.lower() == "yes":
        welcome()
        while attempts > 0 and user_guess != number:
            user_guess = int(input("Enter your guess: "))
            play_game()
            if user_guess == number:
                guesses += 1
                win_game()
                break
        if attempts == 0:
                game_over()
                play_again()
    else:
        print("GAME OVER YOU BOZO !")

welcome()
while attempts > 0 and user_guess != number:
    user_guess = int(input("Enter your guess: "))
    play_game()
    if user_guess == number:
        guesses += 1
        win_game()
        break
if attempts == 0:
    game_over()
    play_again()







