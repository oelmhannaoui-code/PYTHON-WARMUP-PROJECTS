# guess the word
import random

word = ''   # global <- (can be used anywhere)
display = []   # global <-(can be used anywhere)
guessed_letters = []
tries = 10

def welcome():
    print("GUESS THE WORD CHOLO")
def choose_word():
    global word, display
    words = ['youngster', 'practical', 'stoic', 'bamboozle', 'camouflage']
    word = random.choice(words)
    display = ['_'] * len(word)  # ['_', '_', '_', '_', '_', '_']
def show_display():
    print(' '.join(display))  # _ _ _ _ _ _
def play_game():
    global tries
    choose_word()
    while tries > 0 and '_' in display:
        show_display()
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed this letter')
            continue

        guessed_letters.append(guess)

        # check if in word
        if guess in word:
            print('CORRECT ')
            for i in range(len(word)):
                if word[i] == guess:      # READ: what letter is at seat i in the word?
                    display[i] = guess   # WRITE: put that letter at seat i in the display

        else:
           tries -= 1
           print(f'INCORRECT! tries left: {tries}')


#game over
    if '_' not in display:
        print(f'You WIN! the word was {word}')
    else:
        print(f'You LOSE! the word was {word}')

play_game()









