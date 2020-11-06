
secret_word = "wizard"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
# Variables created for the guessing game
# Guess count begins at 0 and guess limit is set to 3 while the boolean out of guesses is set to false for default

while guess != secret_word and not out_of_guesses:
    print("What is is Harry Potter?")
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
# As long as guess isnt equal to the secret word and isnt out of guesses continue asking until correct or out of guesses
# Each incorrect guess adds one to the guess count. If the guess count reaches the limit out of guesses becomes true & L

if out_of_guesses:
    print("Uh oh! Out of guesses, YOU LOSE!")
else:
    print("YOU WIN!")
# Print statements for if you win or loose
